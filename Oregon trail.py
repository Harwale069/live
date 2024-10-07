import time
import sys
import random
import threading
import os

# Global variables
miles_traveled = 0
food = 100
health = 100
money = 300
days_passed = 0
wagon_parts = 0
total_miles = 1000

# Events and their probabilities based on profession
event_chances = {
    "banker": 0.4,
    "hunter": 0.2,
    "farmer": 0.1
}

# List of possible events
events = ["illness", "rest", "hunting", "fishing", "wagon_breakdown", "nothing"]

# Global variable to control the skipping of the typewriter effect
skip_typewriter = False

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter effect function with Enter to skip
def typewriter(text):
    global skip_typewriter
    skip_typewriter = False
    
    def listen_for_skip():
        global skip_typewriter
        input()  # Wait for Enter key
        skip_typewriter = True

    # Start a thread to listen for the Enter key press
    threading.Thread(target=listen_for_skip, daemon=True).start()

    for char in text:
        if skip_typewriter:
            print(text)  # Print the full text immediately
            return
        
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust the speed of typing
        
    print()  # Move to the next line after the text

# Profession selection
def profession_selection():
    clear_screen()
    print("\nChoose your profession:")
    print("1. Banker (Starts with $300, higher chance of bad events as he is rich but not well versed in traveling the trail)")
    print("2. Hunter (Starts with $200, lower chance of mishaps because of the skills he has acquired)")
    print("3. Farmer (Starts with $100, even lower chances of mishaps, he is very skilled but poor)")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        typewriter("You chose Banker! You start with $300!")
        return "banker"
    elif choice == "2":
        typewriter("You chose Hunter! You start with $200!")
        return "hunter"
    elif choice == "3":
        typewriter("You chose Farmer! You start with $100!")
        return "farmer"
    else:
        typewriter("Invalid choice, defaulting to Farmer.")
        return "farmer"

# Travel Phase
def travel_phase(profession):
    global miles_traveled, food, health, days_passed, wagon_parts
    travel_distance = random.randint(15, 30)  # Random distance traveled
    miles_traveled += travel_distance
    food -= random.randint(5, 15)  # Food consumed
    days_passed += 1
    
    # Determine if an event occurs based on profession
    if random.random() < event_chances[profession]:
        event = random.choice(events)
        if event == "illness":
            illness_event()
        elif event == "rest":
            rest_event()
        elif event == "hunting":
            hunting_event()
        elif event == "fishing":
            if miles_traveled % 100 < 30:  # Simulating being near a river
                fishing_event()
            else:
                typewriter("\n🌊 You were not near a river to fish.")
        elif event == "wagon_breakdown":
            wagon_breakdown_event()
        else:
            nothing_event()
    else:
        nothing_event()

# Define events and their outcomes
def illness_event():
    global health
    typewriter("\n😷 You have fallen ill!")
    health -= random.randint(10, 30)
    typewriter(f"Your health is now {health}.")

def rest_event():
    global days_passed, food
    typewriter("\n😴 You decided to take a rest day.")
    days_passed += 1
    food -= 10
    typewriter(f"You have consumed 10 food. Food left: {food}")

def hunting_event():
    global food
    typewriter("\n🏹 You went hunting and found food!")
    food += random.randint(20, 50)
    typewriter(f"Your food is now {food}.")

def fishing_event():
    global food
    typewriter("\n🎣 You went fishing and caught some fish!")
    food += random.randint(15, 40)
    typewriter(f"Your food is now {food}.")

def wagon_breakdown_event():
    global wagon_parts
    typewriter("\n🚨 Your wagon has broken down!")
    wagon_parts -= 1
    typewriter(f"You have lost a wagon part. Remaining: {wagon_parts}")

def nothing_event():
    typewriter("\n✨ Nothing special happened on this leg of the journey.")

# Display the current stats
def display_stats():
    clear_screen()
    print("============================================================")
    print(f"| Name: {player_name} | Miles Traveled: {miles_traveled}/{total_miles} |")
    print(f"| Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed} |")
    print(f"| Wagon Parts: {wagon_parts} | Pace: Normal |")
    print("============================================================")

# Shopping Phase
def shopping_phase():
    global money
    clear_screen()
    print("Before you leave, you can buy supplies.")
    
    while True:
        display_stats()
        print("What would you like to buy? (Enter 'exit' to leave)")
        print("1. Food Store (10 coins per unit)")
        print("2. Medicine Shop (20 coins per health kit)")
        print("3. Gunsmith (50 coins for a gun)")
        print("4. Animal Dealer (100 coins for an oxen or horse)")
        print("5. Wagon Parts Store (30 coins per part)")
        print("Enter your choice (or type 'exit' to leave): ")

        choice = input().lower()
        if choice == 'exit':
            break
        elif choice == '1':
            if money >= 10:
                money -= 10
                typewriter("You bought 1 unit of food!")
            else:
                typewriter("Not enough money!")
        elif choice == '2':
            if money >= 20:
                money -= 20
                typewriter("You bought a health kit!")
            else:
                typewriter("Not enough money!")
        elif choice == '3':
            if money >= 50:
                money -= 50
                typewriter("You bought a gun!")
            else:
                typewriter("Not enough money!")
        elif choice == '4':
            if money >= 100:
                money -= 100
                typewriter("You bought an oxen or horse!")
            else:
                typewriter("Not enough money!")
        elif choice == '5':
            if money >= 30:
                money -= 30
                typewriter("You bought a wagon part!")
            else:
                typewriter("Not enough money!")
        else:
            typewriter("Invalid choice. Please try again.")

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name
    
    player_name = input("Enter your name: ")
    
    if player_name.lower() == "debug224":
        typewriter("Debug mode activated: Infinite resources!")
        global food, health, money, wagon_parts
        food = float("inf")
        health = float("inf")
        money = float("inf")
        wagon_parts = float("inf")
    else:
        profession = profession_selection()  # Select profession before shopping
        shopping_phase()  # Call shopping phase before starting the journey
            
    while miles_traveled < total_miles and health > 0 and food > 0:
        # Display stats
        display_stats()
        
        # Travel phase
        travel_phase(profession)

    # Game over conditions
    if health <= 0:
        typewriter("You have perished due to health complications. Game over.")
    elif food <= 0:
        typewriter("You have run out of food and can no longer continue. Game over.")
    elif miles_traveled >= total_miles:
        typewriter("Congratulations! You have reached your destination!")

# Start the game
if __name__ == "__main__":
    play_game()
