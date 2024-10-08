import random

# Constants for professions
INITIAL_MONEY = {
    "Banker": 36000,
    "Hunter": 24000,
    "Farmer": 12000
}

ITEM_PRICES = {
    "Food": 500,
    "Medicine": 1000,
    "Gun": 2500,
    "Animal": 5000,
    "Wagon Part": 1500,
    "Water": 300,
    "Clothes": 400
}

MAX_HEALTH = 100
DISTANCE_GOAL = 1000

# Player stats
player_name = ""
player_profession = ""
money = 0
food = 100
health = MAX_HEALTH
miles_traveled = 0
wagon_parts = 0
days_passed = 0
animals = 0
guns = 0
medicine = 0
clothes = 0
water = 100

# Game functions
def display_intro():
    print("Welcome to the Oregon Trail!")
    print("Your goal is to travel 1000 miles to the west.")
    print("Survive harsh conditions, manage your resources, and reach your destination.\n")

def choose_profession():
    global player_profession, money
    while True:
        print("Choose your profession:")
        print("1. Banker (Starts with $36,000, more money but higher risk of theft)")
        print("2. Hunter (Starts with $24,000, balanced money and survival skills)")
        print("3. Farmer (Starts with $12,000, least money but lower chance of bad events)")

        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            player_profession = "Banker"
            money = INITIAL_MONEY["Banker"]
            break
        elif choice == '2':
            player_profession = "Hunter"
            money = INITIAL_MONEY["Hunter"]
            break
        elif choice == '3':
            player_profession = "Farmer"
            money = INITIAL_MONEY["Farmer"]
            break
        else:
            print("Invalid choice. Please choose again.")

    print(f"\nYou chose {player_profession}! You start with ${money}.\n")

def display_status():
    print("\n================= Status ==================")
    print(f"| Name: {player_name} | Profession: {player_profession} |")
    print(f"| Miles Traveled: {miles_traveled}/{DISTANCE_GOAL} ({(miles_traveled/DISTANCE_GOAL)*100:.2f}%) |")
    print(f"| Food: {food} | Water: {water} | Clothes: {clothes} |")
    print(f"| Medicine: {medicine} | Guns: {guns} | Animals: {animals} |")
    print(f"| Health: {health}/{MAX_HEALTH} | Money: {money} | Days Passed: {days_passed} |")
    print(f"| Wagon Parts: {wagon_parts} |")
    print("============================================")

def shopping_phase():
    global money, food, health, wagon_parts, animals, guns, medicine, clothes, water
    print("\nBefore you leave, you can buy supplies.")

    while True:
        print("\n--- Shopping Menu ---")
        for index, item in enumerate(ITEM_PRICES.keys(), start=1):
            print(f"{index}. {item} (${ITEM_PRICES[item]} per unit)")

        print("Enter 'exit' to leave the shop.")
        choice = input("What would you like to buy? ")

        if choice.lower() == 'exit':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(ITEM_PRICES):
            item_name = list(ITEM_PRICES.keys())[int(choice) - 1]
            item_price = ITEM_PRICES[item_name]

            while True:
                quantity = input(f"How many {item_name}s would you like to buy? ")
                if quantity.isdigit() and int(quantity) > 0:
                    quantity = int(quantity)
                    total_cost = item_price * quantity
                    if total_cost <= money:
                        money -= total_cost
                        if item_name == "Food":
                            food += quantity
                        elif item_name == "Water":
                            water += quantity
                        elif item_name == "Clothes":
                            clothes += quantity
                        elif item_name == "Medicine":
                            medicine += quantity
                        elif item_name == "Gun":
                            guns += quantity
                        elif item_name == "Animal":
                            animals += quantity
                        elif item_name == "Wagon Part":
                            wagon_parts += quantity
                        print(f"You bought {quantity} {item_name}(s)!")
                        break
                    else:
                        print("You do not have enough money for that!")
                else:
                    print("Please enter a valid positive number.")
        else:
            print("Please select a valid option.")

def random_event():
    global food, health, animals, guns, medicine, water, clothes
    event_type = random.choice(["none", "food_loss", "illness", "water_loss", "animal_loss", "clothing_damage", "theft"])
    
    if event_type == "none":
        print("You encountered no significant events today.")
    elif event_type == "food_loss":
        lost_food = random.randint(10, 30)
        food -= lost_food
        print(f"You lost {lost_food} units of food due to spoilage.")
    elif event_type == "water_loss":
        lost_water = random.randint(10, 30)
        water -= lost_water
        print(f"Some of your water supplies were lost. You lost {lost_water} units.")
    elif event_type == "illness":
        health_loss = random.randint(5, 20)
        health -= health_loss
        print(f"Someone in your party got sick! Health decreased by {health_loss}.")
    elif event_type == "animal_loss":
        if animals > 0:
            animals -= 1
            print("One of your animals died! You lost 1 animal.")
        else:
            print("No animals to lose.")
    elif event_type == "clothing_damage":
        if clothes > 0:
            clothes -= random.randint(1, 5)
            print("Some of your clothes were damaged! You lost a few clothing items.")
        else:
            print("No clothes to lose.")
    elif event_type == "theft":
        stolen_amount = random.randint(500, 3000)
        if money >= stolen_amount:
            money -= stolen_amount
        else:
            money = 0
        print(f"Thieves stole ${stolen_amount} from you!")

def travel():
    global miles_traveled, days_passed, health, food, water
    while miles_traveled < DISTANCE_GOAL and health > 0:
        print("\nTraveling...")
        travel_distance = random.randint(20, 50)  # Travel between 20 and 50 miles
        miles_traveled += travel_distance
        days_passed += random.randint(1, 3)  # Days passed during travel
        food -= random.randint(5, 15)  # Consume food
        water -= random.randint(5, 15)  # Consume water
        health -= random.randint(0, 5)  # Random health loss
        if health < 0:
            health = 0
        if food < 0:
            food = 0
        if water < 0:
            water = 0

        random_event()  # Random events during travel

        display_status()

        if miles_traveled >= DISTANCE_GOAL:
            print("\nCongratulations! You have reached Oregon!")
            break
        elif health <= 0:
            print("\nYour health has dropped to zero. You have failed to reach Oregon.")
            break

def manage_inventory():
    print("\n--- Inventory Management ---")
    print(f"Food: {food} | Water: {water} | Clothes: {clothes}")
    print(f"Guns: {guns} | Medicine: {medicine} | Animals: {animals}")
    print(f"Wagon Parts: {wagon_parts}")
    print("You can trade or reorganize items during rest stops.")

def rest_phase():
    global health, days_passed
    days_rest = random.randint(1, 3)
    days_passed += days_rest
    health_gain = random.randint(10, 30)
    health += health_gain
    if health > MAX_HEALTH:
        health = MAX_HEALTH
    print(f"\nYou rested for {days_rest} days and gained {health_gain} health.")

def main():
    display_intro()
    global player_name
    player_name = input("Enter your name: ")

    choose_profession()
    shopping_phase()

    # Main game loop
    while miles_traveled < DISTANCE_GOAL and health > 0:
        travel()
        if miles_traveled < DISTANCE_GOAL and health > 0:
            print("\nYou have reached a rest stop!")
            print("Would you like to rest (gain health) or continue?")
            choice = input("Enter 'rest' or 'continue': ").lower()
            if choice == 'rest':
                rest_phase()
            manage_inventory()

    print("\nThank you for playing the Oregon Trail!")

if __name__ == "__main__":
    main()
