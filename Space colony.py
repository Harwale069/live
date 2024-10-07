import random

# Introduction
print('''
  _____                         ____      _       _             
 / ____|                       / __ \    | |     | |            
| (___  _ __   __ _  ___ ___  | |  | | __| |_   _| | ___  ___   
 \___ \| '_ \ / _` |/ __/ _ \ | |  | |/ _` | | | | |/ _ \/ __|  
 ____) | |_) | (_| | (_|  __/ | |__| | (_| | |_| | |  __/\__ \  
|_____/| .__/ \__,_|\___\___|  \____/ \__,_|\__,_|_|\___||___/  
       | |                                                      
       |_|                                                      
''')

print("Welcome to your new space colony! Manage your resources and make decisions to help your colony thrive.")
print("Your goal is to survive 100 days and grow your colony as much as possible.\n")

# Game variables
days_survived = 0
food = 100
water = 100
energy = 100
population = 10
morale = 100

# Event functions
def explore():
    gain_food = random.randint(5, 20)
    gain_water = random.randint(5, 20)
    print(f"\nExploration successful! You gained {gain_food} food and {gain_water} water.")
    return gain_food, gain_water

def solar_storm():
    loss_energy = random.randint(10, 30)
    print(f"\nA solar storm hit! You lost {loss_energy} energy.")
    return loss_energy

def disease_outbreak():
    loss_population = random.randint(1, 3)
    morale_loss = random.randint(10, 20)
    print(f"\nA disease outbreak occurred! You lost {loss_population} colonists and {morale_loss} morale.")
    return loss_population, morale_loss

def new_technology():
    gain_energy = random.randint(20, 40)
    morale_gain = random.randint(10, 20)
    print(f"\nYour scientists discovered new technology! You gained {gain_energy} energy and {morale_gain} morale.")
    return gain_energy, morale_gain

# Main game loop
while days_survived < 100 and population > 0 and food > 0 and water > 0 and energy > 0 and morale > 0:
    print(f"\nDay {days_survived + 1}:\n")
    print(f"Population: {population}")
    print(f"Food: {food}")
    print(f"Water: {water}")
    print(f"Energy: {energy}")
    print(f"Morale: {morale}\n")

    # Daily player choice
    print("Choose your action for the day:")
    print("1. Explore for resources")
    print("2. Work on energy production")
    print("3. Rest and boost morale")
    print("4. Expand your colony")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        gain_food, gain_water = explore()
        food += gain_food
        water += gain_water

    elif choice == "2":
        gain_energy = random.randint(15, 30)
        energy += gain_energy
        print(f"\nYour colony worked on energy production. You gained {gain_energy} energy.")

    elif choice == "3":
        morale_boost = random.randint(10, 25)
        morale += morale_boost
        print(f"\nYour colony rested and recovered. You gained {morale_boost} morale.")

    elif choice == "4":
        if food >= 20 and water >= 20:
            food -= 20
            water -= 20
            new_population = random.randint(1, 5)
            population += new_population
            print(f"\nYou expanded your colony! {new_population} new colonists joined.")
        else:
            print("\nNot enough resources to expand your colony. You need at least 20 food and 20 water.")

    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")

    # Random events
    event = random.choice(["solar_storm", "disease_outbreak", "new_technology", "nothing"])
    
    if event == "solar_storm":
        energy_loss = solar_storm()
        energy -= energy_loss
    elif event == "disease_outbreak":
        population_loss, morale_loss = disease_outbreak()
        population -= population_loss
        morale -= morale_loss
    elif event == "new_technology":
        energy_gain, morale_gain = new_technology()
        energy += energy_gain
        morale += morale_gain
    else:
        print("Nothing eventful happened today.")

    # Resource consumption
    food_consumed = population * 2
    water_consumed = population * 2
    food -= food_consumed
    water -= water_consumed

    print(f"\nYour colony consumed {food_consumed} food and {water_consumed} water today.")

    days_survived += 1

    # Check for game over conditions
    if population <= 0:
        print("\nYour colony has perished due to a lack of colonists. Game Over.")
        break
    if food <= 0:
        print("\nYour colony has run out of food. Game Over.")
        break
    if water <= 0:
        print("\nYour colony has run out of water. Game Over.")
        break
    if energy <= 0:
        print("\nYour colony has run out of energy. Game Over.")
        break
    if morale <= 0:
        print("\nYour colony's morale has dropped to zero. The colonists have abandoned the colony. Game Over.")
        break

# Win condition
if days_survived >= 100:
    print(f"\nCongratulations! You've successfully managed your space colony for {days_survived} days.")
else:
    print("\nUnfortunately, you couldn't make it to 100 days.")

