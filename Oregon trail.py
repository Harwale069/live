import random
import time
import sys

# Game variables
player_name = ""
miles_traveled = 0
total_miles = 1000
food = 100
health = 100
days_passed = 0
events = ["illness", "nothing", "rest", "hunting", "fishing"]
supplies = {"food": 0, "medicines": 0}

# Helper functions for displaying the status
def typewriter_effect(text):
    """Simulates a typewriter effect for displaying text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust speed here
    print()

def display_stats():
    typewriter_effect("=" * 60)
    typewriter_effect(f"| Name: {player_name} | Miles Traveled: {miles_traveled}/{total_miles} |")
    typewriter_effect(f"| Food: {food} | Health: {health} | Days Passed: {days_passed} |")
    typewriter_effect("=" * 60)

# Helper function to print the horizontal view
def display_horizontally():
    print(" ")
    print(f"{'-' * miles_traveled}📍{'-' * (total_miles - miles_traveled)}| Oregon")
    print(" ")

# Event functions
def illness_event():
    global health
    illness_damage = random.randint(10, 20)
    health -= illness_damage
    typewriter_effect(f"\n🚑 Oh no! One of your pioneers has fallen ill! Health decreases by {illness_damage}.")

def rest_event():
    global health
    rest_gain = random.randint(5, 15)
    health += rest_gain
    typewriter_effect(f"\n😴 You rested and recovered. You gain {rest_gain} health.")

def hunting_event():
    global food
    food_gain = random.randint(5, 20)
    food += food_gain
    typewriter_effect(f"\n🏹 You went hunting and gained {food_gain} food.")

def fishing_event():
    global food
    food_gain = random.randint(5, 15)
    food += food_gain
    typewriter_effect(f"\n🎣 You went fishing and gained {food_gain} food.")

def nothing_event():
    typewriter_effect("\n😐 Nothing eventful happened today.")

# Shopping function
def shopping():
    global food, supplies
    typewriter_effect("\nWelcome to the General Store! Here are your options:")
    typewriter_effect("1. Buy Food (10 units for $10)")
    typewriter_effect("2. Buy Medicine (heals 20 health for $15)")
    typewriter_effect("3. Leave Store")

    while True:
        choice = input("What would you like to do? (Enter the number): ")
        
        if choice == '1':
            if food >= 10:
                food -= 10
                supplies['food'] += 10
                typewriter_effect("You bought 10 units of food.")
            else:
                typewriter_effect("You don't have enough food to make that purchase.")
        elif choice == '2':
            if food >= 15:
                food -= 15
                supplies['medicines'] += 1
                typewriter_effect("You bought 1 unit of medicine.")
            else:
                typewriter_effect("You don't have enough food to make that purchase.")
        elif choice == '3':
            typewriter_effect("Thank you for visiting the store!")
            break
        else:
            typewriter_effect("Invalid choice. Please select again.")

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name

    typewriter_effect("Welcome to The Oregon Trail!")
    player_name = input("Enter your name: ")
    typewriter_effect(f"Welcome, {player_name}! Your journey to Oregon begins now.\n")
    
    # Pre-departure phase for shopping
    shopping()

    while miles_traveled < total_miles and health > 0 and food > 0:
        # Display stats and horizontal progress
        display_horizontally()
        display_stats()

        # Player travels
        miles_traveled += random.randint(15, 30)
        food -= random.randint(5, 15)
        days_passed += 1

        # Random events
        event = random.choice(events)
        if event == "illness":
            illness_event()
        elif event == "rest":
            rest_event()
        elif event == "hunting":
            hunting_event()
        elif event == "fishing":
            fishing_event()
        else:
            nothing_event()

        time.sleep(1)  # Simulate the passage of time for effect

        # Check for game over conditions
        if health <= 0:
            typewriter_effect("\n💀 Your health has dropped to zero. Game Over.")
            break
        if food <= 0:
            typewriter_effect("\n🍽️ You've run out of food. Game Over.")
            break

    # End of game
    if miles_traveled >= total_miles:
        typewriter_effect(f"\n🏁 Congratulations, {player_name}! You've made it to Oregon!")
    else:
        typewriter_effect(f"\nYou traveled {miles_traveled} miles but did not make it to Oregon.")

# Start the game
play_game()
