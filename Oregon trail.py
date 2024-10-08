import time
import sys
import random
import threading
import os

# Global variables
miles_traveled = 0
food = 100
health = 100
money = 0
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
    print("1. Banker (Starts with $36000, higher chance of bad events as he is rich but not well versed in traveling the trail)")
    print("2. Hunter (Starts with $24000, lower chance of mishaps because of the skills he has acquired)")
    print("3. Farmer (Starts with $12000, even lower chances of mishaps, he is very skilled but poor)")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        typewriter("You chose Banker! You start with $36000!")
        return "banker", 36000
    elif choice == "2":
        typewriter("You chose Hunter! You start with $24000!")
        return "hunter", 24000
    elif choice == "3":
        typewriter("You chose Farmer! You start with $12000!")
        return "farmer", 12000
    else:
        typewriter("Invalid choice, defaulting to Farmer.")
        return "farmer", 12000

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

# Display the current stats, with progress tracker
def display_stats():
    progress_percentage = (miles_traveled / total_miles) * 100
    clear_screen()
    print("============================================================")
    print(f"| Name: {player_name} | Miles Traveled: {miles_traveled}/{total_miles} ({progress_percentage:.2f}%) |")
    print(f"| Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed} |")
    print(f"| Wagon Parts: {wagon_parts} | Pace: Normal |")
    print("============================================================")

# Shopping Phase with item amount selection
def shopping_phase():
    global money, food, health, wagon_parts
    clear_screen()
    print("Before you leave, you can buy supplies.")
    
    while True:
        display_stats()
        print("What would you like to buy? (Enter 'exit' to leave)")
        print("1. Food Store (500 coins per unit)")
        print("2. Medicine Shop (1000 coins per health kit)")
        print("3. Gunsmith (2500 coins for a gun)")
        print("4. Animal Dealer (5000 coins for an oxen or horse)")
        print("5. Wagon Parts Store (1500 coins per part)")
        print("Enter your choice (or type 'exit' to leave): ")

        choice = input().lower()
        if choice == 'exit':
            break
        elif choice in ['1', '2', '3', '4', '5']:
            amount = int(input("How many would you like to buy? "))
            if choice == '1':  # Food
                cost = 500 * amount
                if money >= cost:
                    money -= cost
                    food += amount
                    typewriter(f"You bought {amount} units of food!")
                else:
                    typewriter("Not enough money!")
            elif choice == '2':  # Medicine
                cost = 1000 * amount
                if money >= cost:
                    money -= cost
                    health += 10 * amount  # Each kit restores 10 health
                    typewriter(f"You bought {amount} health kits!")
                else:
                    typewriter("Not enough money!")
            elif choice == '3':  # Guns
                cost = 2500 * amount
                if money >= cost:
                    money -= cost
                    typewriter(f"You bought {amount} guns!")
                else:
                    typewriter("Not enough money!")
            elif choice == '4':  # Animals
                cost = 5000 * amount
                if money >= cost:
                    money -= cost
                    typewriter(f"You bought {amount} animals!")
                else:
                    typewriter("Not enough money!")
            elif choice == '5':  # Wagon parts
                cost = 1500 * amount
                if money >= cost:
                    money -= cost
                    wagon_parts += amount
                    typewriter(f"You bought {amount} wagon parts!")
                else:
                    typewriter("Not enough money!")
        else:
            typewriter("Invalid choice. Please try again.")

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name, money
    
    player_name = input("Enter your name: ")
    
    if player_name.lower() == "debug224":
        typewriter("Debug mode activated: Infinite resources!")
        global food, health, money, wagon_parts
        food = float("inf")
        health = float("inf")
        money = float("inf")
        wagon_parts = float("inf")
    else:
        profession, starting_money = profession_selection()  # Select profession before shopping
        money = starting_money  # Set the starting money based on profession
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
        typewriter("You have run out of food. Starvation ensues. Game over.")
    else:
        typewriter("Congratulations! You reached your destination!")

# Start the game
if __name__ == "__main__":
    play_game()
