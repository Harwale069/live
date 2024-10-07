import time
import sys
import random
import threading

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
    print("\nChoose your profession:")
    print("1. Banker (Starts with $300, higher chance of bad events as he is rich but not well versed in traveling the trail)")
    print("2. Hunter (Starts with $200, lower chance of mishaps because of the skills he has acquired)")
    print("3. Farmer (Starts with $100, even lower chances of mishaps, he is very skilled but poor)")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        typewriter("You chose Banker! You start with $300!")
        return "banker"
    elif choice == '2':
        typewriter("You chose Hunter! You start with $200!")
        return "hunter"
    elif choice == '3':
        typewriter("You chose Farmer! You start with $100!")
        return "farmer"
    else:
        typewriter("Invalid choice, defaulting to Farmer.")
        return "farmer"

# Travel phase
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

# Shopping phase
def shopping_phase():
    global food, money, wagon_parts
    while True:
        print("\nCurrent supplies:")
        print(f"Food: {food} | Money: {money} | Wagon Parts: {wagon_parts}")
        print("What would you like to buy? (Enter 'exit' to leave)")
        print("Food Store: 10 coins")
        print("Medicine Shop: 20 coins")
        print("Gunsmith: 50 coins")
        print("Animal Dealer: 100 coins")
        print("Wagon Parts Store: 30 coins")

        choice = input("Enter your choice (or type the shop name): ").lower()

        if choice == 'exit':
            break
        elif choice == 'food':
            if money >= 10:
                food += 20
                money -= 10
                typewriter("You bought food!")
            else:
                typewriter("Not enough money!")
        elif choice == 'medicine':
            if money >= 20:
                health += 20
                money -= 20
                typewriter("You bought medicine!")
            else:
                typewriter("Not enough money!")
        elif choice == 'gunsmith':
            if money >= 50:
                # Simulate buying a gun
                money -= 50
                typewriter("You bought a gun!")
            else:
                typewriter("Not enough money!")
        elif choice == 'animal':
            if money >= 100:
                # Simulate buying an animal
                money -= 100
                typewriter("You bought an animal!")
            else:
                typewriter("Not enough money!")
        elif choice == 'wagon parts':
            if money >= 30:
                wagon_parts += 1
                money -= 30
                typewriter("You bought wagon parts!")
            else:
                typewriter("Not enough money!")
        else:
            typewriter("Invalid choice, please try again.")

# Event functions
def illness_event():
    global health
    typewriter("You fell ill! Losing health...")
    health -= 20
    typewriter(f"Your health is now {health}.")

def rest_event():
    typewriter("You decided to rest for a day.")
    
def hunting_event():
    global food
    typewriter("You went hunting and found food!")
    food += 20

def fishing_event():
    global food
    typewriter("You went fishing and caught some fish!")
    food += 15

def wagon_breakdown_event():
    global wagon_parts
    typewriter("Your wagon broke down! You need to use wagon parts to fix it.")
    if wagon_parts > 0:
        wagon_parts -= 1
        typewriter("You fixed your wagon.")
    else:
        typewriter("You don't have any wagon parts to fix it!")

def nothing_event():
    typewriter("Nothing happened.")

# Display stats
def display_stats():
    print(f"\nMiles Traveled: {miles_traveled}/{total_miles} | Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed}")

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name

    player_name = input("Enter your name: ")

    if player_name.lower() == "debug224":
        global food, health, money, wagon_parts
        food = float("inf")
        health = float("inf")
        money = float("inf")
        wagon_parts = float("inf")
        typewriter("Debug mode activated: Infinite resources!")
    else:
        profession = profession_selection()  # Select profession before shopping
        shopping_phase()  # Call shopping phase before starting the journey

    while miles_traveled < total_miles and health > 0 and food > 0:
        # Display stats
        display_stats()

        # Travel phase
        travel_phase(profession)

    if miles_traveled >= total_miles:
        typewriter("Congratulations! You've reached Oregon!")
    else:
        typewriter("You ran out of health or food. Game over.")

# Start the game
if __name__ == "__main__":
    play_game()
