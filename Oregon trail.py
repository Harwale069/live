import random

def display_ascii_intro():
    print("""
                ('-. .-.   ('-.                                  
( OO )  / _(  OO)                                 
,--. ,--.(,------.,--.      ,--.      .-'),-----. 
|  | |  | |  .---'|  |.-')  |  |.-') ( OO'  .-.  '
|   .|  | |  |    |  | OO ) |  | OO )/   |  | |  |
|       |(|  '--. |  |`-' | |  |`-' |\_) |  |\|  |
|  .-.  | |  .--'(|  '---.'(|  '---.'  \ |  | |  |
|  | |  | |  `---.|      |  |      |    `'  '-'  '
`--' `--' `------'`------'  `------'      `-----' 
    """)

def display_ascii_end():
    print("""
                                      _ .-') _ .-. .-')                 ('-.   
                                     ( (  OO) )\  ( OO )              _(  OO)  
  ,----.     .-'),-----.  .-'),-----. \     .'_ ;-----.\  ,--.   ,--.(,------. 
 '  .-./-') ( OO'  .-.  '( OO'  .-.  ',`'--..._)| .-.  |   \  `.'  /  |  .---' 
 |  |_( O- )/   |  | |  |/   |  | |  ||  |  \  '| '-' /_).-')     /   |  |     
 |  | .--, \\_) |  |\|  |\_) |  |\|  ||  |   ' || .-. `.(OO  \   /   (|  '--.  
(|  | '. (_/  \ |  | |  |  \ |  | |  ||  |   / :| |  \  ||   /  /\_   |  .--'  
 |  '--'  |    `'  '-'  '   `'  '-'  '|  '--'  /| '--'  /`-./  /.__)  |  `---. 
  `------'       `-----'      `-----' `-------' `------'   `--'       `------'  
    """)

    print("Goodbye! You've reached Oregon successfully!")

def travel_event():
    event = random.choice(['nothing', 'illness', 'hunting', 'fishing', 'foraging', 'resting'])
    
    if event == 'illness':
        print("\nOne of your pioneers has fallen ill! Your health decreases by 12.")
        return -12, 0  # Health loss, food gain
    
    elif event == 'hunting':
        food_gain = random.randint(0, 50)
        print(f"\nYou go hunting... You gained {food_gain} food!")
        return 0, food_gain
    
    elif event == 'fishing':
        food_gain = random.randint(0, 30)
        print(f"\nYou go fishing... You gained {food_gain} food!")
        return 0, food_gain
    
    elif event == 'foraging':
        food_gain = random.randint(0, 20)
        print(f"\nYou forage for food... You gained {food_gain} food!")
        return 0, food_gain
    
    elif event == 'resting':
        health_gain = random.randint(5, 20)
        print(f"\nYou rest and recover... You gain {health_gain} health!")
        return health_gain, 0
    
    else:
        print("\nNothing eventful happened.")
        return 0, 0

def oregon_trail():
    display_ascii_intro()
    
    total_distance = 0
    health = 100
    food = 100
    total_miles = 1000  # Updated distance to 1000 miles
    
    name = input("Enter your name: ")
    print(f"Welcome, {name}! Your journey to Oregon begins now.\n")
    
    while total_distance < total_miles and health > 0 and food > 0:
        # Display current status
        print(f"\nYou've traveled {total_distance} miles. Total distance: {total_distance}/{total_miles} miles.")
        print(f"You have {food} food remaining.")
        print(f"Your health: {health}\n")
        
        # Travel 20 miles per iteration
        total_distance += 20
        food -= 10  # Subtract food as you travel
        
        # Random event
        health_change, food_change = travel_event()
        health += health_change
        food += food_change
        
        if health <= 0:
            print("Your pioneers have died. Game Over.")
            return
        
        if food <= 0:
            print("You've run out of food. Game Over.")
            return
    
    display_ascii_end()

# Run the game
oregon_trail()
