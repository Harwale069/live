import random
import time

# Constants
MAX_HEALTH = 100
INITIAL_MONEY = 100
INITIAL_FOOD = 50
INITIAL_WATER = 40
INITIAL_STAMINA = 100
INITIAL_MORALE = 75
TRAVEL_DISTANCE = 89  # Distance traveled in one travel action
DAYS_PER_TRAVEL = 1
MAX_COMPANIONS = 3
EVENTS = [
    "Found a hidden treasure!",
    "A wild animal attacks!",
    "Met a friendly traveler!",
    "Caught in a storm!",
    "A companion falls ill!",
    "Discovered a useful item!",
    "Faced a difficult choice!",
]
WEATHER_CONDITIONS = ["Sunny", "Rainy", "Snowy", "Windy"]
TRADING_ITEMS = {
    "Food": 10,
    "Water": 5,
    "Tools": 15,
}
RESOURCES = ["Food", "Water", "Ammunition", "Tools"]
MAX_STAMINA = 100

class Player:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.health = MAX_HEALTH
        self.food = INITIAL_FOOD
        self.water = INITIAL_WATER
        self.stamina = INITIAL_STAMINA
        self.morale = INITIAL_MORALE
        self.money = INITIAL_MONEY
        self.miles_traveled = 0
        self.days_passed = 0
        self.companions = []

    def travel(self, pace):
        if pace == "Slow":
            distance = TRAVEL_DISTANCE - 20
        elif pace == "Normal":
            distance = TRAVEL_DISTANCE
        elif pace == "Fast":
            distance = TRAVEL_DISTANCE + 20

        # Adjust health and resources based on travel
        self.miles_traveled += distance
        self.days_passed += DAYS_PER_TRAVEL
        self.food -= 2
        self.water -= 1
        self.stamina -= 10
        self.morale -= random.randint(1, 5)

        if self.stamina < 0:
            self.stamina = 0

        self.random_event()

    def random_event(self):
        event_chance = random.randint(1, 10)
        if event_chance == 1:  # 10% chance of an event
            event = random.choice(EVENTS)
            print(f"Event: {event}")
            if event == "A companion falls ill!":
                if self.companions:
                    ill_companion = random.choice(self.companions)
                    print(f"{ill_companion.name} has fallen ill!")
                    self.morale -= 5
            elif event == "Discovered a useful item!":
                found_item = random.choice(RESOURCES)
                print(f"You found {found_item}!")
                if found_item == "Food":
                    self.food += 10
                elif found_item == "Water":
                    self.water += 10
                elif found_item == "Ammunition":
                    print("You found ammunition!")
                elif found_item == "Tools":
                    print("You found tools!")

    def display_stats(self):
        print(f"Current Stats:\n"
              f"Health: {self.health}\n"
              f"Food: {self.food}\n"
              f"Water: {self.water}\n"
              f"Stamina: {self.stamina}\n"
              f"Morale: {self.morale}\n"
              f"Money: ${self.money}\n"
              f"Miles Traveled: {self.miles_traveled}\n"
              f"Days Passed: {self.days_passed}\n")

    def add_companion(self, companion):
        if len(self.companions) < MAX_COMPANIONS:
            self.companions.append(companion)
            print(f"{companion.name} has joined your party.")
        else:
            print("You cannot have more than 3 companions.")

class Companion:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

def hunt(player):
    if player.food <= 0:
        print("You need food to hunt.")
        return

    hunt_success = random.choice([True, False])
    if hunt_success:
        food_found = random.randint(5, 15)
        player.food += food_found
        print(f"You successfully hunted and found {food_found} units of food!")
    else:
        print("You went hunting but returned empty-handed.")

def fish(player):
    if player.water <= 0:
        print("You need water nearby to fish.")
        return

    fish_success = random.choice([True, False])
    if fish_success:
        fish_caught = random.randint(3, 10)
        player.food += fish_caught
        print(f"You caught {fish_caught} units of fish!")
    else:
        print("You tried to fish but didn't catch anything.")

def check_companions(player):
    if not player.companions:
        print("You have no companions.")
    else:
        print("Your companions:")
        for companion in player.companions:
            print(f"{companion.name} - Skill: {companion.skill}")

def weather_report():
    current_weather = random.choice(WEATHER_CONDITIONS)
    print(f"Current weather: {current_weather}")

def trading_post(player):
    print("Welcome to the Trading Post!")
    print("Available items for trade:")
    for item, price in TRADING_ITEMS.items():
        print(f"{item}: ${price}")

    trade_choice = input("Which item would you like to trade for? (Food, Water, Tools) ")
    if trade_choice in TRADING_ITEMS:
        if player.money >= TRADING_ITEMS[trade_choice]:
            player.money -= TRADING_ITEMS[trade_choice]
            if trade_choice == "Food":
                player.food += 1
            elif trade_choice == "Water":
                player.water += 1
            elif trade_choice == "Tools":
                print("You traded for tools.")
            print(f"You traded for {trade_choice}.")
        else:
            print("You don't have enough money for that item.")
    else:
        print("Invalid choice.")

def camp(player):
    print("You set up camp for the night.")
    player.stamina += 20
    if player.stamina > MAX_STAMINA:
        player.stamina = MAX_STAMINA
    player.food -= 1  # Consuming food for the camp
    print(f"Stamina restored to {player.stamina}. You consumed 1 unit of food.")

def add_companion(player):
    name = input("Enter the name of your companion: ")
    skill = input("Enter the skill of your companion (Hunter, Fisher, Merchant): ")
    companion = Companion(name, skill)
    player.add_companion(companion)

def game_loop():
    name = input("What is your name, traveler? ")
    profession = input("Choose your profession (Hunter, Fisher, Trapper, Merchant): ")
    player = Player(name, profession)

    while True:
        player.display_stats()
        print("Options:")
        print("1. Travel")
        print("2. Save Game (not implemented)")
        print("3. Load Game (not implemented)")
        print("4. Exit Game")
        print("5. Hunt (Requires food)")
        print("6. Fish (Requires water nearby)")
        print("7. Check Companions")
        print("8. Weather Report")
        print("9. Visit Trading Post")
        print("10. Set up Camp")
        print("11. Add Companion")
        
        choice = input("What would you like to do? (1-11): ")

        if choice == "1":
            pace = input("Choose your pace (Normal, Fast, Slow): ")
            player.travel(pace)
        elif choice == "2":
            print("Save Game (not implemented)")
        elif choice == "3":
            print("Load Game (not implemented)")
        elif choice == "4":
            print("Exiting game. Goodbye!")
            break
        elif choice == "5":
            hunt(player)
        elif choice == "6":
            fish(player)
        elif choice == "7":
            check_companions(player)
        elif choice == "8":
            weather_report()
        elif choice == "9":
            trading_post(player)
        elif choice == "10":
            camp(player)
        elif choice == "11":
            add_companion(player)
        else:
            print("Invalid choice. Please choose again.")

# Start the game
if __name__ == "__main__":
    game_loop()
