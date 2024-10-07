import random

# Game setup
print('''
  ('-. .-.   ('-.                                  
 ( OO )  / _(  OO)                                 
 ,--. ,--.(,------.,--.      ,--.      .-'),-----. 
 |  | |  | |  .---'|  |.-')  |  |.-') ( OO'  .-.  '
 |   .|  | |  |    |  | OO ) |  | OO )/   |  | |  |
 |       |(|  '--. |  |`-' | |  |`-' |\_) |  |\|  |
 |  .-.  | |  .--'(|  '---.'(|  '---.'  \ |  | |  |
 |  | |  | |  `---.|      |  |      |    `'  '-'  '
 `--' `--' `------'`------'  `------'      `-----' 
''')

name = input("Enter your name: ")
print(f"Welcome, {name}! Your journey to Oregon begins now.")

# Game variables
distance = 1000
travelled = 0
food = 100
health = 100

# Game loop
while travelled < distance and food > 0:
    print(f"\nYou've traveled {travelled} miles. Total distance: {travelled}/{distance} miles.")
    print(f"You have {food} food remaining.")
    print(f"Your health: {health}")

    # Give the player choices
    print("\nChoose your action:")
    print("1. Continue traveling")
    print("2. Rest")
    print("3. Go hunting")
    print("4. Go fishing")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # Continue traveling
        travelled += random.randint(15, 30)
        food -= 10

        # Random events
        event = random.choice(["illness", "nothing", "recovery"])
        if event == "illness":
            health -= random.randint(10, 20)
            print("\nOne of your pioneers has fallen ill! Your health decreases.")
        elif event == "nothing":
            print("\nNothing eventful happened.")
        elif event == "recovery":
            health += random.randint(5, 15)
            print("\nYou rest and recover... You gain some health!")

    elif choice == "2":
        # Resting
        health += random.randint(5, 15)
        food -= 10
        print("\nYou rest and recover... You gain health but consume food.")
    
    elif choice == "3":
        # Hunting
        gain = random.randint(5, 20)
        food += gain
        print(f"\nYou go hunting... You gained {gain} food!")
    
    elif choice == "4":
        # Fishing
        gain = random.randint(3, 10)
        food += gain
        print(f"\nYou go fishing... You gained {gain} food!")
    
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")

    # Check health and food
    if health <= 0:
        print("\nYour health has dropped to 0. Game Over.")
        break
    if food <= 0:
        print("\nYou've run out of food. Game Over.")
        break

# Game over messages
if travelled >= distance:
    print(f"\nCongratulations, {name}! You've successfully made it to Oregon!")
elif food <= 0:
    print("\nYou've run out of food and couldn't make it to Oregon.")
else:
    print("\nYou couldn't make it to Oregon.")

