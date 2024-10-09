import random
from colorama import Fore, Style

# Constants for professions and difficulties
PROFESSIONS = {
    "Hunter": {
        "pros": ["Increased food availability", "Better animal tracking"],
        "cons": ["Risk of animal attacks", "Requires more stamina"],
        "resource_gain": {"food": 3, "wildlife": 1},
        "market_value": {"food": 2, "tools": 5, "weapons": 10},
    },
    "Fisher": {
        "pros": ["Steady food supply from water", "Better fishing gear"],
        "cons": ["Requires access to water", "Bad weather affects fishing"],
        "resource_gain": {"food": 2, "fish": 3},
        "market_value": {"food": 1, "tools": 5, "weapons": 8},
    },
    "Trapper": {
        "pros": ["Better chance of rare traps", "Stealthy"],
        "cons": ["Takes time to set traps", "Attracts predators"],
        "resource_gain": {"food": 2, "trap": 1},
        "market_value": {"food": 2, "tools": 4, "weapons": 8},
    },
    "Merchant": {
        "pros": ["Profitable trades", "Access to various goods"],
        "cons": ["Can run out of goods", "Less survival skills"],
        "resource_gain": {"trade_goods": 5},
        "market_value": {"food": 1, "tools": 6, "weapons": 12},
    },
    "Blacksmith": {
        "pros": ["Create tools and weapons", "Improved durability"],
        "cons": ["Needs metal resources", "Risk of burns"],
        "resource_gain": {"metal": 2, "tools": 1},
        "market_value": {"food": 1, "tools": 8, "weapons": 15},
    },
    "Doctor": {
        "pros": ["Heal and boost morale", "Better medicine use"],
        "cons": ["High supply usage", "Limited offensive capabilities"],
        "resource_gain": {"medicine": 3, "health_pack": 1},
        "market_value": {"food": 2, "tools": 5, "weapons": 10},
    },
    "Guide": {
        "pros": ["Reduce chances of getting lost", "Better navigation"],
        "cons": ["Less survival skills", "Struggles with hunting"],
        "resource_gain": {"map": 1},
        "market_value": {"food": 2, "tools": 4, "weapons": 10},
    },
}

DIFFICULTY_SETTINGS = {
    "Easy": {"event_weights": [0.5, 0.2, 0.2, 0.1, 0.1]},
    "Normal": {"event_weights": [0.4, 0.3, 0.2, 0.1, 0.1]},
    "Hard": {"event_weights": [0.3, 0.3, 0.2, 0.1, 0.1]},
    "Jameson": {"event_weights": [0.2, 0.4, 0.2, 0.1, 0.1]},
}

# Updated miles and pace
PACE_DISTANCE = {
    "Slow": 10,
    "Normal": 15,
    "Fast": 20
}

# Main shop items
SHOP_ITEMS = {
    "Basic": {"Food": 2, "Tools": 5, "Weapons": 10},
    "Advanced": {"Medicine": 8, "Armor": 15, "Trade Goods": 12}
}

class Player:
    def __init__(self, name, profession, difficulty):
        self.name = name
        self.profession = profession
        self.difficulty = difficulty
        self.health = 100
        self.stamina = 100
        self.miles_traveled = 0
        self.money = 10  # Starting money in historical currency
        self.resources = {"food": 0, "wildlife": 0, "fish": 0, "trap": 0, "trade_goods": 0, "metal": 0, "medicine": 0, "health_pack": 0}
        self.morale = 100  # Morale level
        self.pros = PROFESSIONS[profession]["pros"]
        self.cons = PROFESSIONS[profession]["cons"]

    def display_stats(self):
        print(Fore.GREEN + f"Name: {self.name}, Profession: {self.profession}, Difficulty: {self.difficulty}")
        print(Fore.CYAN + f"Health: {self.health}, Stamina: {self.stamina}, Miles Traveled: {self.miles_traveled}, Money: {self.money}, Morale: {self.morale}")
        print(Fore.YELLOW + "Pros:", ", ".join(self.pros))
        print(Fore.RED + "Cons:", ", ".join(self.cons))
        print(Fore.MAGENTA + "Resources:", self.resources)

    def travel(self, pace):
        miles = PACE_DISTANCE[pace]
        self.miles_traveled += miles
        self.stamina -= miles / 2  # Cost of stamina per mile

        # Determine event based on difficulty
        event = random.choices(
            ["none", "animal encounter", "resource find", "market event", "weather change"],
            weights=DIFFICULTY_SETTINGS[self.difficulty]["event_weights"],
            k=1
        )[0]

        if event == "animal encounter":
            print(Fore.RED + "You encountered a wild animal!")
            self.handle_animal_encounter()
        elif event == "resource find":
            print(Fore.GREEN + "You found some resources on your journey!")
            self.collect_resources()
        elif event == "market event":
            self.handle_market_event()
        elif event == "weather change":
            print(Fore.BLUE + "The weather changed! Travel speed may be affected.")
            self.adjust_for_weather()

        # Update stamina and morale after travel
        if self.stamina < 0:
            self.health -= 10  # Stamina loss affects health
            print(Fore.RED + "You are exhausted! Health decreased.")
        else:
            self.morale += 5  # Successful travel boosts morale
            print(Fore.GREEN + "You traveled successfully and morale improved!")

    def handle_animal_encounter(self):
        print(Fore.RED + "You must decide to fight, flee, or use a trap.")
        choice = input("Choose (fight/flee/trap): ").lower()
        if choice == "fight":
            if random.random() > 0.5:  # 50% chance to succeed
                print(Fore.GREEN + "You defeated the animal!")
                self.resources["wildlife"] += 1
            else:
                self.health -= 20
                print(Fore.RED + "You were injured in the fight!")
        elif choice == "flee":
            print(Fore.YELLOW + "You managed to escape!")
        elif choice == "trap":
            if self.resources["trap"] > 0:
                print(Fore.GREEN + "You successfully trapped the animal!")
                self.resources["wildlife"] += 1
                self.resources["trap"] -= 1
            else:
                print(Fore.RED + "You have no traps available!")
        else:
            print(Fore.RED + "Invalid choice!")

    def handle_market_event(self):
        print(Fore.YELLOW + "You come across a market with fluctuating prices.")
        action = input("Would you like to buy or sell? (buy/sell): ").lower()
        if action == "buy":
            self.buy_items()
        elif action == "sell":
            self.sell_items()
        else:
            print(Fore.RED + "Invalid action!")

    def buy_items(self):
        print(Fore.BLUE + "Available items:")
        for item, price in SHOP_ITEMS["Basic"].items():
            print(f"{item}: {price} coins")
        item_to_buy = input("Which item would you like to buy? ")
        if item_to_buy in SHOP_ITEMS["Basic"]:
            if self.money >= SHOP_ITEMS["Basic"][item_to_buy]:
                self.money -= SHOP_ITEMS["Basic"][item_to_buy]
                self.resources[item_to_buy.lower()] += 1
                print(Fore.GREEN + f"You bought a {item_to_buy}!")
            else:
                print(Fore.RED + "You don't have enough money!")
        else:
            print(Fore.RED + "Invalid item!")

    def sell_items(self):
        print(Fore.BLUE + "Your resources:")
        for item, quantity in self.resources.items():
            if quantity > 0:
                print(f"{item.capitalize()}: {quantity}")
        item_to_sell = input("Which item would you like to sell? ").lower()
        if item_to_sell in self.resources and self.resources[item_to_sell] > 0:
            price = PROFESSIONS[self.profession]["market_value"].get(item_to_sell.capitalize(), 0)
            self.money += price
            self.resources[item_to_sell] -= 1
            print(Fore.GREEN + f"You sold a {item_to_sell} for {price} coins!")
        else:
            print(Fore.RED + "Invalid item or you have none!")

    def adjust_for_weather(self):
        if random.random() < 0.3:  # 30% chance for bad weather
            print(Fore.BLUE + "It's raining heavily, reducing your speed.")
            self.stamina -= 10  # Additional stamina cost for bad weather

    def collect_resources(self):
        for resource, amount in PROFESSIONS[self.profession]["resource_gain"].items():
            self.resources[resource] += amount
        print(Fore.GREEN + "You collected resources: ", self.resources)

def main():
    print(Fore.MAGENTA + "Welcome to the Survival Game!")
    player_name = input("Enter your name: ")
    player_profession = input(f"Choose your profession {list(PROFESSIONS.keys())}: ")
    player_difficulty = input(f"Choose difficulty {list(DIFFICULTY_SETTINGS.keys())}: ")

    player = Player(player_name, player_profession, player_difficulty)

    while player.health > 0 and player.morale > 0:
        player.display_stats()
        pace = input("Choose your pace (Slow/Normal/Fast): ")
        player.travel(pace)

        if player.miles_traveled >= 100:  # Goal to travel 100 miles
            print(Fore.GREEN + f"Congratulations, {player.name}! You've successfully traveled 100 miles!")
            break

    if player.health <= 0:
        print(Fore.RED + "You have died. Game over.")
    elif player.morale <= 0:
        print(Fore.RED + "You have lost your will to survive. Game over.")

if __name__ == "__main__":
    main()
