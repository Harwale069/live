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
    print("Make wise choices and manage your resources well!")
    print("You have a starting balance of ${}.".format(START_MONEY))

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

    distance = random.randint(50, 100)  # Random travel distance
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
    print("3. Medicine ($20 each)")
    print("4. Ammunition ($10 each)")

    choice = input("What would you like to buy? (1-4, or 'exit' to leave): ")
    if choice == "1":
        quantity = int(input("How many food items would you like to buy? "))
        cost = quantity * 5
        if cost <= money:
            money -= cost
            inventory["food"] += quantity
            print("You bought {} food items.".format(quantity))
        else:
            print("You don't have enough money!")
    elif choice == "2":
        quantity = int(input("How many water items would you like to buy? "))
        cost = quantity * 3
        if cost <= money:
            money -= cost
            inventory["water"] += quantity
            print("You bought {} water items.".format(quantity))
        else:
            print("You don't have enough money!")
    elif choice == "3":
        quantity = int(input("How many medicine items would you like to buy? "))
        cost = quantity * 20
        if cost <= money:
            money -= cost
            inventory["medicine"] += quantity
            print("You bought {} medicine items.".format(quantity))
        else:
            print("You don't have enough money!")
    elif choice == "4":
        quantity = int(input("How many ammunition items would you like to buy? "))
        cost = quantity * 10
        if cost <= money:
            money -= cost
            inventory["ammunition"] += quantity
            print("You bought {} ammunition items.".format(quantity))
        else:
            print("You don't have enough money!")
    elif choice.lower() == 'exit':
        print("You leave the merchant's stall.")
    else:
        print("Invalid choice.")

# Function to save the game
def save_game(slot):
    with open(f"{save_file_prefix}{slot}.pkl", "wb") as file:
        pickle.dump((player_name, health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory), file)
    print("Game saved successfully!")

# Function to load the game
def load_game(slot):
    global player_name, health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory
    if os.path.exists(f"{save_file_prefix}{slot}.pkl"):
        with open(f"{save_file_prefix}{slot}.pkl", "rb") as file:
            (player_name, health, food, water, stamina, morale, money, miles_traveled, days_passed, inventory) = pickle.load(file)
        print("Game loaded successfully!")
    else:
        print("Save slot is empty!")

# End game function
def end_game():
    print("Game Over!")
    print("You made it {} miles and survived for {} days.".format(miles_traveled, days_passed))
    print("Thank you for playing!")
    exit()

# Main game loop
def main():
    global player_name
    display_intro()
    player_name = input("What is your name, traveler? ")
    
    while True:
        display_stats()
        print("\nOptions:")
        print("1. Travel")
        print("2. Save Game")
        print("3. Load Game")
        print("4. Exit Game")

        choice = input("What would you like to do? (1-4): ")

        if choice == "1":
            travel()
        elif choice == "2":
            slot = input(f"Enter save slot (1-{SAVE_SLOTS}): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                save_game(slot)
            else:
                print("Invalid save slot!")
        elif choice == "3":
            slot = input(f"Enter save slot to load (1-{SAVE_SLOTS}): ")
            if slot.isdigit() and 1 <= int(slot) <= SAVE_SLOTS:
                load_game(slot)
            else:
                print("Invalid load slot!")
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
