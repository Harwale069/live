import random
import time
import sys

# Game variables
name = ""
profession = ""
food = 100
health = 100
money = 0
wagon_parts = 0
miles_traveled = 0
days_passed = 0
total_miles = 1000
event_chances = {"banker": 0.3, "farmer": 0.1, "hunter": 0.2}
inventory = {"food": 0, "health kit": 0, "gun": 0, "animal": 0}  # Add inventory for items

# Events
events = ["illness", "rest", "hunting", "fishing", "wagon_breakdown"]

# Function for typewriter effect
def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    input("\n(Press Enter to continue)")

# Profession selection
def profession_selection():
    global money
    typewriter("Choose your profession:\n1. Banker (Starts with $300, higher chance of bad events)\n2. Farmer (Starts with $100, lower chance of bad events)\n3. Hunter (Starts with $200, balanced skills)")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        global profession
        profession = "banker"
        money = 300
        typewriter("You chose Banker! You start with $300!")
    elif choice == "2":
        profession = "farmer"
        money = 100
        typewriter("You chose Farmer! You start with $100!")
    elif choice == "3":
        profession = "hunter"
        money = 200
        typewriter("You chose Hunter! You start with $200!")
    else:
        typewriter("Invalid choice, defaulting to Farmer.")
        profession = "farmer"
        money = 100

# Shopping phase
def shopping_phase():
    global money
    typewriter("Before you leave, you can buy supplies.")
    
    # Store items and prices
    store_items = {
        "Food Store": {"food": 10},
        "Medicine Shop": {"health kit": 20},
        "Gunsmith": {"gun": 50},
        "Animal Dealer": {"animal": 100},
        "Wagon Parts Store": {"wagon part": 30}
    }
    
    while True:
        print("Current supplies:")
        print("============================================================")
        print(f"| Name: {name} | Miles Traveled: {miles_traveled}/1000 |")
        print(f"| Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed} |")
        print(f"| Wagon Parts: {wagon_parts} | Pace: Normal |")
        print("============================================================")
        print("What would you like to buy? (Enter 'exit' to leave)")
        
        for store, items in store_items.items():
            for item, price in items.items():
                print(f"{store}: {item.title()} for {price} coins")

        choice = input("Enter your choice (or type the store name): ").lower()
        
        if choice == "exit":
            break
            
        found_item = False
        
        for store, items in store_items.items():
            if choice in store.lower():
                found_item = True
                item_name, price = list(items.items())[0]  # Get first item in store
                quantity = input(f"How many {item_name}s would you like to buy? (Cost: {price} each): ")
                
                try:
                    quantity = int(quantity)
                    total_cost = quantity * price
                    
                    if money >= total_cost:
                        money -= total_cost
                        inventory[item_name] += quantity
                        typewriter(f"You bought {quantity} {item_name}(s)!")
                    else:
                        typewriter("Not enough money!")
                except ValueError:
                    typewriter("Please enter a valid number.")
        
        if not found_item:
            typewriter("Invalid store choice, please try again.")

# Travel Phase
def travel_phase():
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

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name
    
    player_name = input("Enter your name: ")
    
    if player_name.lower() == "debug224":
        global food, health, money, wagon_parts
        food = float("inf")
        health = float("inf")
        money = float("inf")
        inventory = {"food": float("inf"), "health kit": float("inf"), "gun": float("inf"), "animal": float("inf")}
        wagon_parts = float("inf")
        typewriter("Debug mode activated: Infinite resources!")
    else:
        profession_selection()  # Select profession before shopping
        shopping_phase()  # Call shopping phase before starting the journey
            
    while miles_traveled < total_miles and health > 0 and food > 0:
        # Display stats
        display_stats()
                
        # Travel phase
        travel_phase()

    typewriter("Game over! Thanks for playing.")

# Display current stats
def display_stats():
    print("============================================================")
    print(f"| Name: {name} | Miles Traveled: {miles_traveled}/1000 |")
    print(f"| Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed} |")
    print(f"| Wagon Parts: {wagon_parts} | Pace: Normal |")
    print("============================================================")

# Events Placeholder Functions
def illness_event():
    global health
    health -= random.randint(10, 30)
    typewriter("Oh no! You got sick!")

def rest_event():
    global health
    health += 10
    typewriter("You took a rest and recovered some health.")

def hunting_event():
    global food
    food += random.randint(5, 20)
    typewriter("You went hunting and brought back some food.")

def fishing_event():
    global food
    food += random.randint(5, 20)
    typewriter("You fished successfully and caught some food.")

def wagon_breakdown_event():
    global wagon_parts
    wagon_parts += 1
    typewriter("Your wagon broke down! You found a wagon part.")

def nothing_event():
    typewriter("Nothing happened on your journey.")

# Start the game
if __name__ == "__main__":
    play_game()
