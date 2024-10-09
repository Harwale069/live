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
            print("You were injured during the encounter!")
    
    elif event == "A storm is approaching.":
        health -= 5
        stamina -= 5
        print("You lost health and stamina due to the storm.")
    
    elif event == "You meet a stranger who offers you food.":
        food += 15
        morale += 10
        print("A kind stranger gave you food and boosted your morale!")
    
    elif event == "You find a river to rest by.":
        health += 10
        stamina += 10
        print("You rested by the river and regained health and stamina.")
    
    elif event == "A band of hostile travelers attacks you!":
        if random.random() < 0.5:
            health -= 20
            money_lost = random.randint(10, 30)
            money -= money_lost
            print(f"You were attacked and lost ${money_lost}. Health decreased.")
        else:
            ammunition = random.randint(5, 15)
            inventory["ammunition"] += ammunition
            print(f"You fended off the attackers and gained {ammunition} ammunition.")
    
    elif event == "You find an abandoned cabin.":
        resources = random.choice(["medicine", "tools", "food", "water"])
        if resources == "food":
            food += 20
        elif resources == "water":
            water += 15
        else:
            inventory[resources] += 1
        print(f"You found an abandoned cabin and scavenged for supplies: {resources}")
    
    elif event == "You discover a hidden stash of supplies.":
        stash_money = random.randint(20, 50)
        money += stash_money
        print(f"You found a hidden stash of supplies and gained ${stash_money}.")
    
    elif event == "You stumble upon a lost traveler who needs help.":
        if random.random() < 0.5:
            print("You helped the traveler and they rewarded you with supplies!")
            food += 10
            water += 10
            morale += 5
        else:
            health -= 5
            print("You tried to help, but it didn't go as planned. You lost some health.")
    
    elif event == "You experience a miraculous turn of luck!":
        health += 10
        morale += 15
        print("Your luck has turned around! Health and morale increased.")
    
    elif event == "A local merchant offers rare goods.":
        print("The merchant has offered you special items for trade.")
        trade_menu()

# Merchant Trading
def trade_menu():
    global money, food, water, inventory
    while True:
        print("\nMerchant Trading:")
        print("1. Buy Special Food Pack ($50)")
        print("2. Buy Clean Water ($20)")
        print("3. Buy Premium Medicine ($30)")
        print("4. Buy Quality Tools ($25)")
        print("5. Leave the Merchant")
        
        choice = input("What would you like to buy? (1-5): ")
        
        if choice == '1':
            if money >= 50:
                food += 25
                money -= 50
                print("You purchased a Special Food Pack.")
            else:
                print("You don't have enough money!")
        elif choice == '2':
            if money >= 20:
                water += 10
                money -= 20
                print("You purchased Clean Water.")
            else:
                print("You don't have enough money!")
        elif choice == '3':
            if money >= 30:
                inventory["medicine"] += 1
                money -= 30
                print("You purchased Premium Medicine.")
            else:
                print("You don't have enough money!")
        elif choice == '4':
            if money >= 25:
                inventory["tools"] += 1
                money -= 25
                print("You purchased Quality Tools.")
            else:
                print("You don't have enough money!")
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please choose again.")

# Status function
def display_status():
    print("\nCurrent Status:")
    print(f"Health: {health}")
    print(f"Food: {food}")
    print(f"Water: {water}")
    print(f"Stamina: {stamina}")
    print(f"Morale: {morale}")
    print(f"Money: ${money}")
    print(f"Miles Traveled: {miles_traveled}/{DISTANCE_GOAL}")
    print(f"Days Passed: {days_passed}")
    print("Inventory:", inventory)

# Game over check
def check_game_over():
    global health
    if health <= 0:
        print("You have succumbed to the dangers of the Oregon Trail. Game Over.")
        return True
    elif miles_traveled >= DISTANCE_GOAL:
        print("Congratulations! You have reached Oregon!")
        return True
    return False

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
        'recent_actions': recent_actions
    }
    with open(f"{save_file_prefix}{slot}.pkl", "wb") as f:
        pickle.dump(save_data, f)
    print(f"Game saved in slot {slot}.")

# Load game function
def load_game(slot):
    global player_name, health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory, recent_actions
    try:
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
        print(f"Game loaded from slot {slot}.")
    except FileNotFoundError:
        print(f"No save found in slot {slot}.")

# Main game loop
def main():
    global player_name
    clear_screen()
    display_intro()
    player_name = input("Enter your name: ")
    set_difficulty()
    color_theme = select_color_theme()
    
    while True:
        clear_screen()
        print(color_theme + f"Welcome, {player_name}! Current Theme: {color_theme}")
        display_status()
        action = input("What would you like to do next? (travel, save, load, status, exit): ").strip().lower()
        
        if action == "travel":
            travel()
            if check_game_over():
                break
        elif action == "save":
            slot = input("Select save slot (1-5): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                save_game(slot)
            else:
                print("Invalid slot! Please choose a slot between 1 and 5.")
        elif action == "load":
            slot = input("Select load slot (1-5): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                load_game(slot)
            else:
                print("Invalid slot! Please choose a slot between 1 and 5.")
        elif action == "status":
            display_status()
        elif action == "exit":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid action! Please choose again.")

if __name__ == "__main__":
    main()
