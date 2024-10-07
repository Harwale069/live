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
money = 100
inventory = {}
wagon_parts = 0
pace = "normal"  # Can be "slow", "normal", or "fast"
towns = ["Independence", "Fort Kearny", "Chimney Rock", "Fort Laramie", "South Pass", "Soda Springs", "Fort Boise", "Oregon City"]
events = ["illness", "nothing", "rest", "hunting", "fishing", "wagon_breakdown"]

# Helper functions
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line after the text

def display_stats():
    print("=" * 60)
    print(f"| Name: {player_name} | Miles Traveled: {miles_traveled}/{total_miles} |")
    print(f"| Food: {food} | Health: {health} | Money: {money} | Days Passed: {days_passed} |")
    print(f"| Wagon Parts: {wagon_parts} | Pace: {pace.capitalize()} |")
    print("=" * 60)

def display_horizontally():
    progress = miles_traveled / total_miles * 100
    bar_length = 50
    filled_length = int(bar_length * progress // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"{bar}📍 {'Oregon'}")
    print(" ")

# Event functions
def illness_event():
    global health
    illness_damage = random.randint(10, 20)
    health -= illness_damage
    typewriter(f"\n🚑 Oh no! One of your pioneers has fallen ill! Health decreases by {illness_damage}.")

def rest_event():
    global health
    rest_gain = random.randint(5, 15)
    health += rest_gain
    typewriter(f"\n😴 You rested and recovered. You gain {rest_gain} health.")

def hunting_event():
    global food
    food_gain = random.randint(5, 20)
    food += food_gain
    typewriter(f"\n🏹 You went hunting and gained {food_gain} food.")

def fishing_event():
    global food
    food_gain = random.randint(5, 15)
    food += food_gain
    typewriter(f"\n🎣 You went fishing and gained {food_gain} food.")

def nothing_event():
    typewriter("\n😐 Nothing eventful happened today.")

def wagon_breakdown_event():
    global wagon_parts, money
    if wagon_parts > 0:
        wagon_parts -= 1
        typewriter("\n🚧 Your wagon broke down! You used one wagon part to repair it.")
    else:
        typewriter("\n💔 Your wagon broke down! You're stranded and have no parts to repair it. Game Over.")

# Shopping Phase
def shopping_phase():
    global food, health, money, wagon_parts
    typewriter("\nBefore you leave, you can buy supplies.")
    
    shops = {
        "Food Store": {"food": 10, "price": 10},
        "Medicine Shop": {"health": 20, "price": 20},
        "Gunsmith": {"gun": 50, "price": 50},
        "Animal Dealer": {"animal": 100, "price": 100},
        "Wagon Parts Store": {"wagon_part": 30, "price": 30}
    }

    while True:
        typewriter("\nCurrent supplies:")
        display_stats()
        typewriter("What would you like to buy? (Enter 'exit' to leave)")

        for shop in shops:
            item = shops[shop]
            typewriter(f"{shop}: {item.keys()} for {item['price']} coins")

        choice = input("Enter your choice (or type the shop name): ").strip().lower()
        
        if choice == "exit":
            break
        
        for shop, item in shops.items():
            if choice in item.keys():
                if money >= item["price"]:
                    money -= item["price"]
                    inventory[choice] = inventory.get(choice, 0) + 1
                    if choice == "wagon_part":
                        wagon_parts += 1
                    typewriter(f"You bought a {choice}!")
                else:
                    typewriter("You don't have enough money.")
                break
        else:
            typewriter("Invalid choice, please try again.")

# Profession Selection
def profession_selection():
    global money
    typewriter("\nChoose your profession:")
    typewriter("1. Banker (Starts with $200)")
    typewriter("2. Farmer (Starts with $100)")
    typewriter("3. Hunter (Starts with $100)")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        money += 100
        typewriter("You chose Banker! You start with $200!")
    elif choice == "2":
        typewriter("You chose Farmer! You start with $100!")
    elif choice == "3":
        typewriter("You chose Hunter! You start with $100!")
    else:
        typewriter("Invalid choice, defaulting to Farmer.")

# Travel Phase
def travel_phase():
    global miles_traveled, food, health, days_passed, wagon_parts
    travel_distance = random.randint(15, 30)  # Random distance traveled
    miles_traveled += travel_distance
    food -= random.randint(5, 15)  # Food consumed
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
        if miles_traveled % 100 < 30:  # Simulating being near a river
            fishing_event()
        else:
            typewriter("\n🌊 You were not near a river to fish.")
    elif event == "wagon_breakdown":
        wagon_breakdown_event()
    else:
        nothing_event()

# Main game loop
def play_game():
    global miles_traveled, food, health, days_passed, player_name

    player_name = input("Enter your name: ")
    
    if player_name.lower() == "debug224":
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
        # Display stats and horizontal progress
        display_horizontally()
        display_stats()

        # Travel phase
        travel_phase()
        time.sleep(1)  # Simulate the passage of time for effect

        # Check for game over conditions
        if health <= 0:
            typewriter("\n💀 Your health has dropped to zero. Game Over.")
            break
        if food <= 0:
            typewriter("\n🍽️ You've run out of food. Game Over.")
            break
        if wagon_parts <= 0 and miles_traveled < total_miles:
            typewriter("\n🚧 You cannot continue without wagon parts! Game Over.")

    # End of game
    if miles_traveled >= total_miles:
        typewriter(f"\n🏁 Congratulations, {player_name}! You've made it to Oregon!")
    else:
        typewriter(f"\nYou traveled {miles_traveled} miles but did not make it to Oregon.")

# Start the game
play_game()
