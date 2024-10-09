import random

# Hunting mechanism
def hunt():
    global food
    print("You go hunting...")
    success = random.choice([True, False])
    if success:
        food_gained = random.randint(10, 50)
        food += food_gained
        print(f"You successfully hunted and gained {food_gained} units of food!")
    else:
        print("You failed to catch any food. Better luck next time!")

# Fishing mechanism
def fish():
    global food
    print("You go fishing...")
    if water > 0:
        success = random.choice([True, False])
        if success:
            food_gained = random.randint(5, 30)
            food += food_gained
            print(f"You caught some fish and gained {food_gained} units of food!")
        else:
            print("You didn't catch any fish this time.")
    else:
        print("You need to be near a water source to fish.")

# Check companions
def check_companions():
    if companions:
        print("Your companions are:")
        for companion in companions:
            print(f"- {companion}")
    else:
        print("You have no companions.")

# Start the game
if __name__ == "__main__":
    main()
