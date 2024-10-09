import random
import time

# Constants
DISTANCE_GOAL = 1000  # Total distance to travel (miles)
START_HEALTH = 100
START_FOOD = 50
START_WATER = 40
START_MONEY = 100
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
            print("You couldn't help the traveler in time, and your morale suffered.")
            morale -= 10
    
    elif event == "You experience a miraculous turn of luck!":
        print("Fortune smiles upon you! You gain extra resources.")
        food += 20
        water += 15
        morale += 10
        money += 50
    
    elif event == "A local merchant offers rare goods.":
        print("You can trade with the merchant!")
        trade_with_merchant()

# Shop for supplies
def trade_with_merchant():
    global food, water, money, inventory
    print("\nThe merchant has the following items:")
    print("1. Special Food Pack (10 units for $25)")
    print("2. Clean Water (10 units for $20)")
    print("3. Premium Medicine ($30 per unit)")
    print("4. Quality Tools ($25 each)")
    
    while True:
        choice = input("What would you like to trade for? (1-4) or 5 to exit: ")
        if choice == '1':
            if money >= 25:
                food += 10
                money -= 25
                print("You purchased a Special Food Pack!")
            else:
                print("You don't have enough money.")
        elif choice == '2':
            if money >= 20:
                water += 10
                money -= 20
                print("You purchased Clean Water!")
            else:
                print("You don't have enough money.")
        elif choice == '3':
            if money >= 30:
                inventory["medicine"] += 1
                money -= 30
                print("You purchased Premium Medicine!")
            else:
                print("You don't have enough money.")
        elif choice == '4':
            if money >= 25:
                inventory["tools"] += 1
                money -= 25
                print("You purchased Quality Tools!")
            else:
                print("You don't have enough money.")
        elif choice == '5':
            print("You leave the merchant.")
            break
        else:
            print("Invalid choice!")

# Display player status
def display_status():
    clear_screen()
    print("Player Status:")
    print(f"Name: {player_name}")
    print(f"Health: {health}")
    print(f"Food: {food}")
    print(f"Water: {water}")
    print(f"Stamina: {stamina}")
    print(f"Morale: {morale}")
    print(f"Money: ${money}")
    print(f"Miles Traveled: {miles_traveled} miles")
    print(f"Days Passed: {days_passed} days")
    print(f"Inventory: {inventory}")
    print("-" * 50)

# Profession selection
def choose_profession():
    global player_name
    player_name = input("Enter your name: ")
    print("Choose your profession:")
    print("1. Doctor (Health specialist)")
    print("2. Farmer (Food specialist)")
    print("3. Hunter (Food and survival expert)")
    print("4. Jameson (Newbie)")

    while True:
        profession_choice = input("Your choice (1-4): ")
        if profession_choice == '1':
            print("You have chosen Doctor!")
            # Doctor benefits
            global START_HEALTH
            START_HEALTH += 20
            break
        elif profession_choice == '2':
            print("You have chosen Farmer!")
            # Farmer benefits
            global START_FOOD
            START_FOOD += 20
            break
        elif profession_choice == '3':
            print("You have chosen Hunter!")
            # Hunter benefits
            global START_FOOD, START_MONEY
            START_FOOD += 10
            START_MONEY += 20
            break
        elif profession_choice == '4':
            print("You have chosen Jameson! Good luck!")
            # Jameson starts with lower stats
            START_HEALTH -= 30
            START_FOOD -= 20
            START_WATER -= 10
            break
        else:
            print("Invalid choice! Please choose again.")

# Main game loop
def game_loop():
    global health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory
    choose_profession()
    set_difficulty()
    while health > 0 and miles_traveled < DISTANCE_GOAL:
        display_status()
        print("Choose an action:")
        print("1. Travel")
        print("2. Check Status")
        print("3. Rest")
        print("4. Trade with Merchant")
        print("5. Exit Game")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            travel()
        elif choice == '2':
            display_status()
        elif choice == '3':
            rest()
        elif choice == '4':
            trade_with_merchant()
        elif choice == '5':
            print("Thank you for playing! Safe travels.")
            break
        else:
            print("Invalid choice, please try again.")
    
    if health <= 0:
        print("You have succumbed to your injuries and failed the journey.")
    elif miles_traveled >= DISTANCE_GOAL:
        print("Congratulations! You have reached your destination and survived the Oregon Trail!")

# Rest function
def rest():
    global health, stamina, food, morale
    clear_screen()
    print("You choose to rest.")
    stamina += 30
    health += 20
    morale += 5
    food -= 5  # Resting consumes some food
    if food < 0:
        food = 0
        health -= 5
        print("You ran out of food while resting! Health decreased.")
    print("You feel refreshed after resting!")

# Run the game
if __name__ == "__main__":
    game_loop()
