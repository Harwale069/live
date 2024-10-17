import random
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value.")

def display_header(title):
    print(Fore.MAGENTA + "\n" + "*" * 40)
    print(Fore.MAGENTA + f"    {title}")
    print(Fore.MAGENTA + "*" * 40)

def ohms_law_challenge():
    display_header("Ohm's Law Challenge")
    I = random.randint(1, 10)  # Current in Amperes
    R = random.randint(1, 20)  # Resistance in Ohms
    V = I * R  # Calculate Voltage

    print(Fore.CYAN + f"Given a current (I) of {I} A and a resistance (R) of {R} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the voltage (V)? ")

    if abs(answer - V) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {V} V.")
        return False

def circuit_connection_challenge():
    display_header("Circuit Connection Challenge")
    connections = ["A) Series", "B) Parallel"]
    print(Fore.CYAN + "What type of circuit connects components end-to-end?")
    for option in connections:
        print(option)

    answer = input(Fore.GREEN + "Your answer (A or B): ").strip().upper()

    if answer == "A":
        print(Fore.GREEN + "Correct! Series circuits connect components end-to-end.")
        return True
    else:
        print(Fore.RED + "Wrong! The correct answer is A) Series.")
        return False

def wiring_challenge():
    display_header("Wiring Challenge")
    colors = {
        "A": "Black - Hot Wire",
        "B": "White - Neutral Wire",
        "C": "Green - Ground Wire",
        "D": "Red - Hot Wire"
    }
    print(Fore.CYAN + "Which color wire is typically used for the ground wire?")
    for option, color in colors.items():
        print(f"{option}) {color}")

    answer = input(Fore.GREEN + "Your answer (A, B, C, or D): ").strip().upper()

    if answer == "C":
        print(Fore.GREEN + "Correct! Green is the color for the ground wire.")
        return True
    else:
        print(Fore.RED + "Wrong! The correct answer is C) Green.")
        return False

def power_calculation_challenge():
    display_header("Power Calculation Challenge")
    V = random.randint(10, 120)  # Voltage in Volts
    I = random.randint(1, 15)     # Current in Amperes
    P = V * I  # Calculate Power

    print(Fore.CYAN + f"Given a voltage (V) of {V} V and a current (I) of {I} A,")
    answer = get_float_input(Fore.GREEN + "What is the power (P) in watts? ")

    if abs(answer - P) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {P} W.")
        return False

def series_resistance_challenge():
    display_header("Series Resistance Challenge")
    R1 = random.randint(1, 10)
    R2 = random.randint(1, 10)
    total_resistance = R1 + R2  # Total resistance in series

    print(Fore.CYAN + f"Given two resistors in series: R1 = {R1} Ω and R2 = {R2} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the total resistance (R_total)? ")

    if abs(answer - total_resistance) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {total_resistance} Ω.")
        return False

def parallel_resistance_challenge():
    display_header("Parallel Resistance Challenge")
    R1 = random.randint(1, 20)
    R2 = random.randint(1, 20)

    total_resistance = (R1 * R2) / (R1 + R2)  # Total resistance in parallel

    print(Fore.CYAN + f"Given two resistors in parallel: R1 = {R1} Ω and R2 = {R2} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the total resistance (R_total)? ")

    if abs(answer - total_resistance) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {total_resistance:.2f} Ω.")
        return False

def labeling_challenge():
    display_header("Labeling Challenge")
    print(Fore.CYAN + """
    Here is a simple circuit diagram:

         (A)          (B)
       ┌───┐        ┌───┐
       │ R │        │ R │
       │ 1 │        │ 2 │
       └───┘        └───┘
         │            │
         │            │
      ┌──┴──┐     ┌───┴───┐
      │     │     │       │
  ┌───┴───┐ │     │       │
  │       │ │     │       │
  │       │ │     │       │
  └───────┘ │     └───────┘
     (C)     │        (D)
      │       │
      └───────┘
     (E)
    """)

    labels = {
        "A": "Resistor 1",
        "B": "Resistor 2",
        "C": "Power Source (+)",
        "D": "Power Source (-)",
        "E": "Ground"
    }

    for option, label in labels.items():
        answer = input(Fore.GREEN + f"What does {option} represent? ").strip().capitalize()
        if answer == label:
            print(Fore.GREEN + "Correct!")
        else:
            print(Fore.RED + f"Wrong! {option} represents {label}.")

def capacitor_challenge():
    display_header("Capacitor Challenge")
    C1 = random.randint(1, 10)  # Capacitance in microfarads
    C2 = random.randint(1, 10)  # Capacitance in microfarads
    total_capacitance = C1 + C2  # Total capacitance in series

    print(Fore.CYAN + f"Given two capacitors in series: C1 = {C1} µF and C2 = {C2} µF,")
    answer = get_float_input(Fore.GREEN + "What is the total capacitance (C_total)? ")

    if abs(answer - total_capacitance) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
    else:
        print(Fore.RED + f"Wrong! The correct answer is {total_capacitance} µF.")

def transformer_challenge():
    display_header("Transformer Challenge")
    primary_voltage = random.randint(100, 240)  # Primary voltage
    turns_ratio = random.uniform(1, 3)  # Turns ratio
    secondary_voltage = primary_voltage * turns_ratio  # Calculate secondary voltage

    print(Fore.CYAN + f"Given a primary voltage of {primary_voltage} V and a turns ratio of {turns_ratio:.2f},")
    answer = get_float_input(Fore.GREEN + "What is the secondary voltage (V_s)? ")

    if abs(answer - secondary_voltage) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
    else:
        print(Fore.RED + f"Wrong! The correct answer is {secondary_voltage:.2f} V.")

def start_screen():
    print(Fore.MAGENTA + "*" * 40)
    print(Fore.MAGENTA + "*  Welcome to the Electrical Engineering  *")
    print(Fore.MAGENTA + "*            Interactive Game            *")
    print(Fore.MAGENTA + "*" * 40)
    print(Fore.YELLOW + "Get ready to test your knowledge and skills!")
    print(Fore.YELLOW + "Press Enter to begin...")
    input()
    print(Fore.MAGENTA + "\n" + "*" * 40)
    time.sleep(1)

def interactive_game():
    start_screen()
    score = 0
    challenges = [
        ohms_law_challenge,
        circuit_connection_challenge,
        wiring_challenge,
        power_calculation_challenge,
        series_resistance_challenge,
        parallel_resistance_challenge,
        labeling_challenge,
        capacitor_challenge,
        transformer_challenge
    ]

    random.shuffle(challenges)

    for challenge in challenges:
        if challenge():
            score += 1
        time.sleep(1)

    print(Fore.CYAN + f"\nYour final score is: {score}/{len(challenges)}")
    print(Fore.MAGENTA + "Thank you for playing!")

if __name__ == "__main__":
    interactive_game()
