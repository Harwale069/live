import random
import time

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Calculator function for math-related questions
def calculator_mode():
    print(f"{CYAN}--- Calculator Mode ---{RESET}")
    print("You can now use the calculator for help with calculations.")
    while True:
        expression = input("Enter the calculation (e.g., '5 + 3 * 2') or type 'exit' to quit: ")
        if expression.lower() == 'exit':
            break
        try:
            result = eval(expression)
            print(f"{GREEN}Result: {result}{RESET}\n")
        except:
            print(f"{RED}Invalid calculation! Please enter a valid expression.{RESET}\n")

# Flashcard mode for review
def flashcard_mode():
    flashcards = [
        {"question": "What is Ohm's Law formula?", "answer": "V = I * R"},
        {"question": "What is the power formula?", "answer": "P = V * I"},
        {"question": "What is the unit of current?", "answer": "Ampere (A)"},
        {"question": "What type of wire is typically red?", "answer": "Hot wire"},
        {"question": "What is the formula for total resistance in series?", "answer": "R_total = R1 + R2"},
        {"question": "What is the formula for total resistance in parallel?", "answer": "1/R_total = 1/R1 + 1/R2"},
        {"question": "What color is the ground wire?", "answer": "Green"},
        {"question": "What type of circuit connects components end-to-end?", "answer": "Series"},
    ]
    print(f"{CYAN}Welcome to Flashcards Mode!{RESET}")
    input("Press Enter to begin flipping cards...\n")
    random.shuffle(flashcards)
    for card in flashcards:
        print(f"{YELLOW}Q: {card['question']}{RESET}")
        input("Press Enter to see the answer...")
        print(f"{GREEN}A: {card['answer']}{RESET}\n")
        input("Press Enter to continue...\n")

# Quiz function with calculator and skip option
def quiz_with_skip():
    challenges = [
        {
            "question": "Given two resistors in series: R1 = 5 Ω and R2 = 3 Ω, what is the total resistance (R_total)?",
            "answer": 8,
            "explanation": "The total resistance in series is the sum of R1 and R2: 5 Ω + 3 Ω = 8 Ω."
        },
        {
            "question": "Given a primary voltage of 131 V and a turns ratio of 1.57, what is the secondary voltage (V_s)?",
            "answer": 206.04,
            "explanation": "The secondary voltage is calculated using the formula V_secondary = V_primary * turns ratio."
        },
        {
            "question": "Given a voltage (V) of 34 V and a current (I) of 1 A, what is the power (P) in watts?",
            "answer": 34,
            "explanation": "Power is calculated using P = V * I, so 34 V * 1 A = 34 W."
        },
        {
            "question": "Which color wire is typically used for the ground wire?\nA) Black - Hot Wire\nB) White - Neutral Wire\nC) Green - Ground Wire\nD) Red - Hot Wire",
            "answer": "C",
            "explanation": "Green is the color used for the ground wire."
        },
        {
            "question": "Given two capacitors in series: C1 = 5 µF and C2 = 5 µF, what is the total capacitance (C_total)?",
            "answer": 2.5,
            "explanation": "Capacitances in series combine as 1/C_total = 1/C1 + 1/C2."
        }
    ]

    score = 0
    total_questions = len(challenges)
    for challenge in challenges:
        print(f"{BLUE}{challenge['question']}{RESET}")
        user_input = input("Your answer (or type 'skip' to skip this question, or 'calc' for the calculator): ")
        
        if user_input.lower() == 'skip':
            print(f"{YELLOW}You chose to skip this question.{RESET}\n")
            continue
        elif user_input.lower() == 'calc':
            calculator_mode()
            user_input = input("Now enter your answer: ")

        try:
            if float(user_input) == float(challenge['answer']):
                print(f"{GREEN}Correct! Well done.{RESET}\n")
                score += 1
            else:
                print(f"{RED}Wrong! The correct answer is {challenge['answer']}.{RESET}\n")
        except ValueError:
            if user_input.upper() == challenge['answer']:
                print(f"{GREEN}Correct! Well done.{RESET}\n")
                score += 1
            else:
                print(f"{RED}Wrong! The correct answer is {challenge['answer']}.{RESET}\n")

        print(f"{CYAN}Explanation: {challenge['explanation']}{RESET}\n")
        time.sleep(1)

    print(f"{CYAN}Your final score is: {score}/{total_questions}{RESET}\n")

# Main game loop
def main():
    print(f"{YELLOW}****************************************{RESET}")
    print(f"{YELLOW}*         Welcome to Alex Harwood's       *{RESET}")
    print(f"{YELLOW}* Electrical Engineering  Interactive Game*{RESET}")
    print(f"{YELLOW}****************************************{RESET}")
    input(f"{CYAN}Press Enter to begin...{RESET}\n")

    while True:
        print(f"{GREEN}Choose a mode:{RESET}")
        print("1. Challenge Mode")
        print("2. Flashcards Mode")
        print("3. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            quiz_with_skip()
        elif choice == '2':
            flashcard_mode()
        elif choice == '3':
            print(f"{GREEN}Thank you for playing!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please select again.{RESET}\n")

# Run the game
main()
