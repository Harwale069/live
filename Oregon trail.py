import time
import pickle
import os
import random
from threading import Thread

# Constants
START_MONEY = 100
DISTANCE_GOAL = 1000
START_HEALTH = 100
START_FOOD = 50
START_WATER = 40
START_STAMINA = 100
START_MORALE = 75
FOOD_PER_TRAVEL = 10
WATER_PER_TRAVEL = 5
STAMINA_PER_TRAVEL = 10
MORALE_LOSS_TRAVEL = 5
EVENT_COUNTDOWN = 3
DEBUG_MODE = False

# Events, terrains, and professions
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
PROFESSIONS = ["Hunter", "Fisher", "Trapper", "Merchant", "Traveler"]

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
companions = []
event_counter = EVENT_COUNTDOWN
difficulty = ""
pace = "Normal"

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

# ASCII visuals
ASCII_VIEWS = {
    "river": r"""
         ~ ~ ~
       ~       ~
     ~~~~~~~~~~~~
    """,
    "cabin": r"""
        ___
       /   \
      |     |
      |_____|
    """,
}

# Game save slots
SAVE_SLOTS = 5
save_file_prefix = "save_game_"

# Function to run a separate console for displaying actions
def run_console():
    while True:
        print(f"Current Stats: Health: {health}, Food: {food}, Water: {water}, Stamina: {stamina}, Morale: {morale}, Money: {money}, Miles Traveled: {miles_traveled}, Days Passed: {days_passed}")
        time.sleep(3)

# Introduction
def display_intro():
    print("Welcome to Oregon Trail Deluxe Edition!")
    print("Your goal is to survive the treacherous journey to Oregon.")
    print("Make wise choices and manage your resources well!")
    print("You have a starting balance of ${}.".format(START_MONEY))
    choose_profession()

# Profession selection
def choose_profession():
    global profession
    print("Choose your profession:")
    for i, profession in enumerate(PROFESSIONS):
        print(f"{i + 1}. {profession}")
    choice = int(input("Enter the number of your choice: ")) - 1
    profession = PROFESSIONS[choice]

# Display player stats
def display_stats():
    print("\nCurrent Stats:")
    print("Health: {}".format(health))
    print("Food: {}".format(food))
    print("Water: {}".format(water))
    print("Stamina: {}".format(stamina))
    print("Morale: {}".format(morale))
    print("Money: ${}".format(money))
    print("Miles Traveled: {}".format(miles_traveled))
    print("Days Passed: {}".format(days_passed))

# Function to handle traveling
def travel():
    global miles_traveled, food, water, stamina, morale, days_passed, event_counter

    if food <= 0 or water <= 0 or stamina <= 0:
        print("You can't travel anymore. You need food, water, or rest!")
        return

    # Change pace based on player choice
    pace_choice = input("Choose your pace (Normal, Fast, Slow): ")
    global pace
    pace = pace_choice if pace_choice in ["Normal", "Fast", "Slow"] else "Normal"

    distance = random.randint(50, 100)  # Random travel distance
    if pace == "Fast":
        distance *= 1.5
        stamina -= 15
    elif pace == "Slow":
        distance *= 0.75
        stamina -= 5

    miles_traveled += distance
    food -= FOOD_PER_TRAVEL
    water -= WATER_PER_TRAVEL
    stamina -= STAMINA_PER_TRAVEL
    morale -= MORALE_LOSS_TRAVEL
    days_passed += 1
    event_counter -= 1

    print("\nYou traveled {} miles.".format(distance))
    print("You have {} miles left to reach Oregon.".format(DISTANCE_GOAL - miles_traveled))

    # Check if an event occurs
    if event_counter <= 0:
        trigger_event()
        event_counter = EVENT_COUNTDOWN

    # Check if player reaches goal
    if miles_traveled >= DISTANCE_GOAL:
        print("Congratulations! You've reached Oregon!")
        end_game()

# Function to trigger random events
def trigger_event():
    event = random.choice(EVENTS)
    print("\nEvent: " + event)

    if event == EVENTS[0]:  # Wild animal encounter
        handle_wild_animal()
    elif event == EVENTS[1]:  # Storm
        handle_storm()
    elif event == EVENTS[2]:  # Stranger offers food
        handle_stranger()
    elif event == EVENTS[3]:  # Find a river
        handle_river()
    elif event == EVENTS[4]:  # Hostile travelers
        handle_hostile_travelers()
    elif event == EVENTS[5]:  # Abandoned cabin
        handle_abandoned_cabin()
    elif event == EVENTS[6]:  # Hidden stash
        handle_hidden_stash()
    elif event == EVENTS[7]:  # Lost traveler
        handle_lost_traveler()
    elif event == EVENTS[8]:  # Turn of luck
        handle_turn_of_luck()
    elif event == EVENTS[9]:  # Merchant offers goods
        handle_merchant()

# Event handlers
def handle_wild_animal():
    global health, morale
    print("You encounter a wild animal! You lose 10 health.")
    health -= 10
    morale -= 5
    display_stats()

def handle_storm():
    global stamina
    print("A storm is approaching! You lose 10 stamina.")
    stamina -= 10
    display_stats()

def handle_stranger():
    global food
    print("A stranger offers you food. You gain 20 food.")
    food += 20
    display_stats()

def handle_river():
    print("You find a river to rest by. Your morale improves by 10.")
    print(ASCII_VIEWS["river"])
    global morale
    morale += 10
    display_stats()

def handle_hostile_travelers():
    global health, morale
    print("A band of hostile travelers attacks you! You lose 20 health and 10 morale.")
    health -= 20
    morale -= 10
    display_stats()

def handle_abandoned_cabin():
    global food, water
    print("You find an abandoned cabin. You gain 30 food and 20 water.")
    print(ASCII_VIEWS["cabin"])
    food += 30
    water += 20
    display_stats()

def handle_hidden_stash():
    global money
    print("You discover a hidden stash of supplies! You gain $50.")
    money += 50
    display_stats()

def handle_lost_traveler():
    print("You stumble upon a lost traveler who needs help. Your morale improves by 10.")
    global morale
    morale += 10
    display_stats()

def handle_turn_of_luck():
    global money
    print("You experience a miraculous turn of luck! You gain $100.")
    money += 100
    display_stats()

def handle_merchant():
    print("A local merchant offers rare goods. You can buy supplies.")
    print("1. Food ($5 each)")
    print("2. Water ($3 each)")
    print("3. Medicine ($10 each)")
    choice = input("Choose an item to buy (1-3) or type 'exit' to leave: ")
    if choice == '1':
        quantity = int(input("How many units of food would you like to buy? "))
        total_cost = quantity * 5
        if money >= total_cost:
            money -= total_cost
            global food
            food += quantity
            print(f"You bought {quantity} units of food.")
        else:
            print("You don't have enough money!")
    elif choice == '2':
        quantity = int(input("How many units of water would you like to buy? "))
        total_cost = quantity * 3
        if money >= total_cost:
            money -= total_cost
            global water
            water += quantity
            print(f"You bought {quantity} units of water.")
        else:
            print("You don't have enough money!")
    elif choice == '3':
        quantity = int(input("How many units of medicine would you like to buy? "))
        total_cost = quantity * 10
        if money >= total_cost:
            money -= total_cost
            inventory["medicine"] += quantity
            print(f"You bought {quantity} units of medicine.")
        else:
            print("You don't have enough money!")
    elif choice == 'exit':
        print("You chose to leave the merchant.")
    else:
        print("Invalid choice.")

# Function to save the game
def save_game(slot):
    save_file = f"{save_file_prefix}{slot}.pkl"
    with open(save_file, 'wb') as f:
        pickle.dump((health, food, water, stamina, morale, money, miles_traveled, days_passed, companions, event_counter, pace), f)
    print("Game saved successfully!")

# Function to load a saved game
def load_game(slot):
    global health, food, water, stamina, morale, money, miles_traveled, days_passed, companions, event_counter, pace
    save_file = f"{save_file_prefix}{slot}.pkl"
    if os.path.exists(save_file):
        with open(save_file, 'rb') as f:
            (health, food, water, stamina, morale, money, miles_traveled, days_passed, companions, event_counter, pace) = pickle.load(f)
        print("Game loaded successfully!")
    else:
        print("No save file found.")

# Function to end the game
def end_game():
    print("Thank you for playing Oregon Trail Deluxe Edition!")
    exit()

# Main game loop
def main():
    global player_name
    player_name = input("Enter your name: ")
    display_intro()

    # Start console thread
    console_thread = Thread(target=run_console)
    console_thread.start()

    while True:
        print("\nWhat would you like to do?")
        print("1. Travel")
        print("2. Check stats")
        print("3. Save game")
        print("4. Load game")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            travel()
        elif choice == '2':
            display_stats()
        elif choice == '3':
            slot = input(f"Choose a save slot (1-{SAVE_SLOTS}): ")
            save_game(slot)
        elif choice == '4':
            slot = input(f"Choose a load slot (1-{SAVE_SLOTS}): ")
            load_game(slot)
        elif choice == '5':
            end_game()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
