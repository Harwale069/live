import random
import time
import pickle
import os

# Constants
START_MONEY = 100  # Define your starting money amount
DISTANCE_GOAL = 1000  # Total distance to travel (miles)
START_HEALTH = 100
START_FOOD = 50
START_WATER = 40
START_STAMINA = 100
START_MORALE = 75
FOOD_PER_TRAVEL = 10
WATER_PER_TRAVEL = 5
STAMINA_PER_TRAVEL = 10
MORALE_LOSS_TRAVEL = 5
EVENT_COUNTDOWN = 3  # Days until another event occurs

# Events and locations
EVENTS = [
    "You encounter a wild animal!",
    "A storm is approaching.",
    "You meet a stranger who offers you food.",
    "You find a river to rest by.",
    "A band of hostile travelers attacks you!",
    "You find an abandoned cabin.",
    "You discover a hidden stash of supplies.",
    "You stumble upon a lost traveler who needs help.",
    "You experience a miraculous turn of luck!",
    "A local merchant offers rare goods."
]

TERRAINS = ["Desert", "Forest", "Mountains", "Plains", "River"]
WEATHERS = ["Sunny", "Rainy", "Snowy", "Windy"]

# Player stats
player_name = ""
health = START_HEALTH
food = START_FOOD
water = START_WATER
stamina = START_STAMINA
morale = START_MORALE
money = START_MONEY
miles_traveled = 0
days_passed = 0
inventory = {"medicine": 0, "ammunition": 0, "tools": 0}
recent_actions = []
event_counter = EVENT_COUNTDOWN
difficulty = ""
jameson_mode = False

# Color themes
THEMES = {
    "default": "\033[0m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}

# Game save slots
SAVE_SLOTS = 5
save_file_prefix = "save_game_"

# Introduction
def display_intro():
    print("Welcome to Oregon Trail Deluxe Edition!")
    print("Your goal is to survive the treacherous journey to Oregon.")
    print("Along the way, you must manage your resources, make tough decisions, and survive random events.")
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Jameson (Special Challenge)")
    print("-" * 50)

# Clear screen
def clear_screen():
    print("\n" * 5)

# Difficulty settings
def set_difficulty():
    global difficulty, jameson_mode
    while True:
        choice = input("Select difficulty (1-4): ")
        if choice == '1':
            difficulty = "Easy"
            print("You have selected Easy difficulty.")
            break
        elif choice == '2':
            difficulty = "Medium"
            print("You have selected Medium difficulty.")
            break
        elif choice == '3':
            difficulty = "Hard"
            print("You have selected Hard difficulty.")
            break
        elif choice == '4':
            difficulty = "Jameson"
            jameson_mode = True
            print("You have selected Jameson difficulty.")
            break
        else:
            print("Invalid choice! Please choose again.")

# Select color theme
def select_color_theme():
    print("Choose a color theme:")
    for i, theme in enumerate(THEMES.keys(), 1):
        print(f"{i}. {theme.capitalize()}")
    choice = input("Select a theme (1-{}): ".format(len(THEMES)))
    if choice.isdigit() and 1 <= int(choice) <= len(THEMES):
        return list(THEMES.values())[int(choice) - 1]
    else:
        print("Invalid choice! Default theme selected.")
        return THEMES["default"]

# Store function
def store_menu():
    global money
    store_items = {
        "Special Food Pack": {"price": 50, "description": "A pack filled with high-quality food."},
        "Clean Water": {"price": 20, "description": "Pure and refreshing water."},
        "Premium Medicine": {"price": 30, "description": "Essential for treating injuries."},
        "Quality Tools": {"price": 25, "description": "Useful for repairs and crafting."},
        "Survival Kit": {"price": 75, "description": "Contains various tools and supplies for survival."},
        "First Aid Kit": {"price": 60, "description": "Heals wounds and restores health."}
    }
    
    print("\nWelcome to the Merchant's Store!")
    print("Available items for purchase:")
    for item, details in store_items.items():
        print(f"{item}: ${details['price']} - {details['description']}")
    
    while True:
        choice = input("\nWhich item would you like to buy? (Enter item name or 'exit' to leave): ")
        
        if choice == "exit":
            print("Thank you for visiting the store!")
            break
        elif choice in store_items:
            item_price = store_items[choice]['price']
            if money >= item_price:
                money -= item_price
                if choice == "Special Food Pack":
                    food += 25
                elif choice == "Clean Water":
                    water += 10
                elif choice == "Premium Medicine":
                    inventory["medicine"] += 1
                elif choice == "Quality Tools":
                    inventory["tools"] += 1
                elif choice == "Survival Kit":
                    food += 15
                    water += 5
                    inventory["tools"] += 1
                elif choice == "First Aid Kit":
                    health += 20
                print(f"You purchased {choice}.")
            else:
                print("You don't have enough money!")
        else:
            print("Invalid choice! Please choose again.")

# Travel function
def travel():
    global miles_traveled, health, food, water, stamina, morale, days_passed, event_counter
    clear_screen()
    print("You decide to continue your journey.")
    
    # Determine travel distance and terrain/weather effects
    if jameson_mode:
        terrain = "River"
        miles_this_trip = random.randint(10, 30)  # Limited distance
        health -= 10  # Always a risk in the river
        print("You're traveling in a river.")
    else:
        miles_this_trip = random.randint(30, 70)
        terrain = random.choice(TERRAINS)
    
    weather = random.choice(WEATHERS)
    
    print(f"You're traveling through {terrain} under {weather} weather.")
    
    if terrain == "Mountains":
        miles_this_trip -= 10
        stamina -= 15
        print("The mountains are tough to navigate, reducing your progress.")
    
    if weather == "Snowy":
        health -= 10
        stamina -= 10
        print("The cold weather takes a toll on your health and stamina.")
    
    miles_traveled += miles_this_trip
    days_passed += 1
    event_counter -= 1
    
    # Resource consumption
    food -= FOOD_PER_TRAVEL
    water -= WATER_PER_TRAVEL
    stamina -= STAMINA_PER_TRAVEL
    morale -= MORALE_LOSS_TRAVEL
    
    if food < 0:
        food = 0
        health -= 10
        recent_actions.append("You ran out of food! Health decreased.")
    
    if water < 0:
        water = 0
        health -= 10
        recent_actions.append("You ran out of water! Health decreased.")
    
    if stamina < 0:
        stamina = 0
        health -= 10
        recent_actions.append("You are exhausted! Health decreased.")
    
    # Trigger random event
    if event_counter <= 0:
        random_event()
        event_counter = EVENT_COUNTDOWN  # Reset the event counter

# Random events
def random_event():
    global health, food, water, morale, money, inventory
    
    event = random.choice(EVENTS)
    
    # Adjust event consequences based on difficulty
    if jameson_mode:
        bad_event_chance = 0.8  # 80% chance of a bad event
    else:
        bad_event_chance = 0.2 if difficulty == "Easy" else 0.5 if difficulty == "Medium" else 0.7
        
    if random.random() < bad_event_chance:
        event = random.choice(EVENTS[0:5])  # Only bad events
    
    if event == "You encounter a wild animal!":
        print("\nA wild animal attacks!")
        if random.random() < 0.5:  # 50% chance to win the encounter
            food_gained = random.randint(10, 20)
            food += food_gained
            print(f"You hunted successfully and gained {food_gained} units of food.")
        else:
            health -= 10
            print("You were injured while trying to escape!")
    
    elif event == "A storm is approaching.":
        print("\nA storm hits your camp!")
        morale -= 10
        health -= 5
        print("You lose morale and some health.")
    
    elif event == "You meet a stranger who offers you food.":
        print("\nA stranger approaches and offers you food.")
        if random.random() < 0.5:  # 50% chance to accept
            food_gained = random.randint(15, 30)
            food += food_gained
            print(f"You accepted the offer and gained {food_gained} units of food.")
        else:
            print("You declined the offer, wary of the stranger.")
    
    elif event == "You find a river to rest by.":
        print("\nYou find a river and decide to rest.")
        water += 20
        stamina += 20
        print("You gain water and stamina from the rest.")
    
    elif event == "A band of hostile travelers attacks you!":
        print("\nHostile travelers attack your camp!")
        health -= 20
        morale -= 15
        print("You suffered injuries and lost morale.")
    
    elif event == "You find an abandoned cabin.":
        print("\nYou discover an abandoned cabin!")
        inventory["tools"] += 2
        print("You find tools in the cabin.")
    
    elif event == "You discover a hidden stash of supplies.":
        print("\nYou discover a stash of supplies!")
        food += 50
        water += 30
        print("You gain food and water.")
    
    elif event == "You stumble upon a lost traveler who needs help.":
        print("\nA lost traveler approaches you for help.")
        if random.random() < 0.5:  # 50% chance to help
            morale += 10
            print("You helped the traveler, and your morale increased.")
        else:
            print("You ignored the traveler and continued on your way.")
    
    elif event == "You experience a miraculous turn of luck!":
        print("\nYou experience a miracle!")
        money += 50
        print("You found $50 in your path!")
    
    elif event == "A local merchant offers rare goods.":
        print("\nA merchant approaches with rare goods!")
        if random.random() < 0.7:  # 70% chance to buy
            if money >= 40:
                money -= 40
                food += 20
                print("You purchased food from the merchant.")
            else:
                print("You don't have enough money to buy from the merchant.")
        else:
            print("You decided not to buy anything.")

# Save game function
def save_game(slot):
    save_data = {
        'player_name': player_name,
        'health': health,
        'food': food,
        'water': water,
        'stamina': stamina,
        'morale': morale,
        'money': money,
        'miles_traveled': miles_traveled,
        'days_passed': days_passed,
        'inventory': inventory,
        'recent_actions': recent_actions,
        'difficulty': difficulty,
        'jameson_mode': jameson_mode
    }
    with open(f"{save_file_prefix}{slot}.pkl", "wb") as f:
        pickle.dump(save_data, f)
    print(f"Game saved in slot {slot}.")

# Load game function
def load_game(slot):
    global player_name, health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory, recent_actions, difficulty, jameson_mode
    with open(f"{save_file_prefix}{slot}.pkl", "rb") as f:
        save_data = pickle.load(f)
        player_name = save_data['player_name']
        health = save_data['health']
        food = save_data['food']
        water = save_data['water']
        stamina = save_data['stamina']
        morale = save_data['morale']
        money = save_data['money']
        miles_traveled = save_data['miles_traveled']
        days_passed = save_data['days_passed']
        inventory = save_data['inventory']
        recent_actions = save_data['recent_actions']
        difficulty = save_data['difficulty']
        jameson_mode = save_data['jameson_mode']
    print(f"Game loaded from slot {slot}.")

# Main game loop
def main_game_loop():
    global player_name
    player_name = input("Enter your name: ")
    clear_screen()
    display_intro()
    set_difficulty()
    
    while miles_traveled < DISTANCE_GOAL:
        clear_screen()
        print(f"Distance Traveled: {miles_traveled}/{DISTANCE_GOAL} miles")
        print(f"Health: {health}, Food: {food}, Water: {water}, Stamina: {stamina}, Morale: {morale}, Money: {money}")
        print("Recent Actions:")
        for action in recent_actions[-5:]:
            print(f"- {action}")
        
        print("\nWhat would you like to do?")
        print("1. Travel")
        print("2. Visit the Store")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Exit Game")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            travel()
        elif choice == '2':
            store_menu()
        elif choice == '3':
            slot = input(f"Select save slot (1-{SAVE_SLOTS}): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                save_game(slot)
            else:
                print("Invalid slot!")
        elif choice == '4':
            slot = input(f"Select load slot (1-{SAVE_SLOTS}): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                load_game(slot)
            else:
                print("Invalid slot!")
        elif choice == '5':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice! Please select again.")
        time.sleep(1)

# Start the game
if __name__ == "__main__":
    main_game_loop()
