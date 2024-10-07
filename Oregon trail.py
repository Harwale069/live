import random
import time

# Game settings
player_name = ""
distance_to_travel = 200  # Total distance to Oregon
current_distance = 0
health = 100
food = 100
pioneers = 5

# ASCII Art for visuals
ascii_art = {
    "start": r"""
        __        __          _   _       _       
        \ \      / /         | | | |     | |      
         \ \ /\ / /__  _ __| |_| |_ ___| |_ ___ 
          \ V  V / _ \| '__| __| __/ _ \ __/ _ \
           \_/\_/_/ \_\_|  \__|\__\___/\__\___/ 
                                                  
    """,
    "camp": r"""
        / \   
       / _ \  
      | (_) | 
       \___/  
    """,
    "hunting": r"""
        ,    ,    ,
        |\   |\   |\
        | \  | \  | \
        |  \ |  \ |  \
       (    ) (    ) ( 
        `--'   `--'   `--' 
    """,
    "sick": r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/ 
    """,
    "end": r"""
         ______  _   _  _______  _____    _____  _    _ 
        |  ____|| \ | ||  __ \ \ \   / /  / ____|| |  | |
        | |__   |  \| || |  | | \ \_/ /  | (___  | |__| |
        |  __|  | . ` || |  | |  \   /    \___ \ |  __  |
        | |____ | |\  || |__| |   | |     ____) || |  | |
        |______||_| \_||_____/    |_|    |_____/ |_|  |_|
    """
}

def print_slow(str):
    """Prints a string slowly for effect."""
    for char in str:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def travel():
    global current_distance, health, food, pioneers
    while current_distance < distance_to_travel and health > 0 and pioneers > 0:
        print(ascii_art["camp"])
        print_slow(f"You've traveled 20 miles. Total distance: {current_distance + 20}/{distance_to_travel} miles.")
        current_distance += 20
        food -= random.randint(5, 15)  # Decrease food supplies
        print_slow(f"You have {food} food remaining.")
        
        # Random events
        event = random.choice(["nothing", "hunting", "sick"])
        if event == "hunting":
            hunt()
        elif event == "sick":
            get_sick()

        # Check for food
        if food <= 0:
            print_slow("You have run out of food and your party is starving!")
            pioneers -= random.randint(1, 3)  # Lose some pioneers
            print_slow(f"Remaining pioneers: {pioneers}")

        # Check health
        if health <= 0:
            print_slow("Your party has succumbed to sickness!")
            pioneers = 0

def hunt():
    global food
    print(ascii_art["hunting"])
    print_slow("You go hunting...")
    hunt_outcome = random.choice(["success", "failure"])
    if hunt_outcome == "success":
        food_gain = random.randint(10, 50)
        food += food_gain
        print_slow(f"You successfully hunted and gained {food_gain} food!")
    else:
        print_slow("You failed to catch any game.")

def get_sick():
    global health, pioneers
    print(ascii_art["sick"])
    print_slow("One of your pioneers has fallen ill!")
    health_loss = random.randint(10, 30)
    health -= health_loss
    print_slow(f"Your health decreased by {health_loss}. Current health: {health}.")
    if random.random() < 0.3:  # 30% chance to lose a pioneer
        pioneers -= 1
        print_slow("One of your pioneers has died from the illness.")
        print_slow(f"Remaining pioneers: {pioneers}")

def end_game():
    if health <= 0 or pioneers <= 0:
        print_slow("Your journey has come to an unfortunate end.")
    else:
        print_slow("Congratulations! You've reached Oregon!")
    print(ascii_art["end"])

def main():
    global player_name
    print(ascii_art["start"])
    player_name = input("Enter your name: ")
    print_slow(f"Welcome, {player_name}! Your journey to Oregon begins now.")
    travel()
    end_game()

if __name__ == "__main__":
    main()
