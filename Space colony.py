import random

class SpaceColony:
    def __init__(self):
        self.population = 100
        self.resources = 200
        self.happiness = 75
        self.turn = 1

    def print_status(self):
        print(f"Turn: {self.turn}")
        print(f"Population: {self.population}")
        print(f"Resources: {self.resources}")
        print(f"Happiness: {self.happiness}\n")

    def make_decision(self):
        print("Choose an action:")
        print("1. Build new housing (+10 population, -20 resources)")
        print("2. Explore new land (+30 resources, -10 happiness)")
        print("3. Organize a festival (+20 happiness, -10 resources)")
        print("4. Skip turn")

        choice = input("Enter the number of your choice: ")
        if choice == '1':
            self.build_housing()
        elif choice == '2':
            self.explore_land()
        elif choice == '3':
            self.organize_festival()
        elif choice == '4':
            print("You skipped your turn.\n")
        else:
            print("Invalid choice! Turn skipped.\n")

    def build_housing(self):
        if self.resources >= 20:
            self.population += 10
            self.resources -= 20
            print("You built new housing! +10 population, -20 resources.\n")
        else:
            print("Not enough resources to build housing.\n")

    def explore_land(self):
        self.resources += 30
        self.happiness -= 10
        print("You explored new land! +30 resources, -10 happiness.\n")

    def organize_festival(self):
        if self.resources >= 10:
            self.happiness += 20
            self.resources -= 10
            print("You organized a festival! +20 happiness, -10 resources.\n")
        else:
            print("Not enough resources to organize a festival.\n")

    def next_turn(self):
        self.turn += 1
        self.population += random.randint(-5, 5)  # Random event affecting population
        self.resources -= random.randint(5, 15)   # Random event affecting resources
        self.happiness += random.randint(-5, 5)   # Random event affecting happiness

        # Check for win/lose conditions
        if self.population <= 0:
            print("Your colony population has died out. Game Over.")
            return False
        if self.resources <= 0:
            print("Your colony has run out of resources. Game Over.")
            return False
        if self.happiness <= 0:
            print("Your colony's happiness has dropped too low. Game Over.")
            return False

        return True

def run_game():
    colony = SpaceColony()
    
    while True:
        colony.print_status()
        colony.make_decision()
        if not colony.next_turn():
            break
    print("Thanks for playing the Space Colony Simulator!")

if __name__ == "__main__":
    run_game()
