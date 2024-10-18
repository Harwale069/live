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

def ohms_law_explanation(I, R):
    V = I * R
    print(Fore.CYAN + f"Ohm's Law states that Voltage (V) = Current (I) × Resistance (R).")
    print(Fore.CYAN + f"So, with a current of {I} A and resistance of {R} Ω, the voltage is {V} V.")
    return V

def power_explanation(V, I):
    P = V * I
    print(Fore.CYAN + f"Power (P) is calculated as Voltage (V) × Current (I).")
    print(Fore.CYAN + f"With a voltage of {V} V and current of {I} A, the power is {P} watts.")
    return P

def resistance_series_explanation(R1, R2):
    total_resistance = R1 + R2
    print(Fore.CYAN + "In a series circuit, the total resistance is the sum of all resistances.")
    print(Fore.CYAN + f"Therefore, R_total = R1 + R2 = {R1} Ω + {R2} Ω = {total_resistance} Ω.")
    return total_resistance

def resistance_parallel_explanation(R1, R2):
    total_resistance = (R1 * R2) / (R1 + R2)
    print(Fore.CYAN + "In a parallel circuit, the total resistance is calculated using:")
    print(Fore.CYAN + "1/R_total = 1/R1 + 1/R2.")
    print(Fore.CYAN + f"The total resistance is {total_resistance:.2f} Ω.")
    return total_resistance

def capacitor_explanation(C1, C2):
    total_capacitance = C1 + C2
    print(Fore.CYAN + "For capacitors in series, the total capacitance is the sum of all capacitances.")
    print(Fore.CYAN + f"Thus, C_total = C1 + C2 = {C1} µF + {C2} µF = {total_capacitance} µF.")
    return total_capacitance

def transformer_explanation(primary_voltage, turns_ratio):
    secondary_voltage = primary_voltage * turns_ratio
    print(Fore.CYAN + "In transformers, the secondary voltage is calculated using the turns ratio.")
    print(Fore.CYAN + f"V_secondary = V_primary × Turns_ratio.")
    print(Fore.CYAN + f"With V_primary = {primary_voltage} V and Turns_ratio = {turns_ratio:.2f},")
    print(Fore.CYAN + f"V_secondary = {secondary_voltage:.2f} V.")
    return secondary_voltage

def ohms_law_challenge():
    display_header("Ohm's Law Challenge")
    I = random.randint(1, 10)  # Current in Amperes
    R = random.randint(1, 20)  # Resistance in Ohms
    print(Fore.CYAN + f"Given a current (I) of {I} A and a resistance (R) of {R} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the voltage (V)? ")

    correct_answer = ohms_law_explanation(I, R)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer} V.")
        return False

def power_calculation_challenge():
    display_header("Power Calculation Challenge")
    V = random.randint(10, 120)  # Voltage in Volts
    I = random.randint(1, 15)     # Current in Amperes
    print(Fore.CYAN + f"Given a voltage (V) of {V} V and a current (I) of {I} A,")
    answer = get_float_input(Fore.GREEN + "What is the power (P) in watts? ")

    correct_answer = power_explanation(V, I)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer} W.")
        return False

def series_resistance_challenge():
    display_header("Series Resistance Challenge")
    R1 = random.randint(1, 10)
    R2 = random.randint(1, 10)
    print(Fore.CYAN + f"Given two resistors in series: R1 = {R1} Ω and R2 = {R2} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the total resistance (R_total)? ")

    correct_answer = resistance_series_explanation(R1, R2)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer} Ω.")
        return False

def parallel_resistance_challenge():
    display_header("Parallel Resistance Challenge")
    R1 = random.randint(1, 20)
    R2 = random.randint(1, 20)
    print(Fore.CYAN + f"Given two resistors in parallel: R1 = {R1} Ω and R2 = {R2} Ω,")
    answer = get_float_input(Fore.GREEN + "What is the total resistance (R_total)? ")

    correct_answer = resistance_parallel_explanation(R1, R2)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer:.2f} Ω.")
        return False

def capacitor_challenge():
    display_header("Capacitor Challenge")
    C1 = random.randint(1, 10)  # Capacitance in microfarads
    C2 = random.randint(1, 10)  # Capacitance in microfarads
    print(Fore.CYAN + f"Given two capacitors in series: C1 = {C1} µF and C2 = {C2} µF,")
    answer = get_float_input(Fore.GREEN + "What is the total capacitance (C_total)? ")

    correct_answer = capacitor_explanation(C1, C2)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer} µF.")
        return False

def transformer_challenge():
    display_header("Transformer Challenge")
    primary_voltage = random.randint(100, 240)  # Primary voltage
    turns_ratio = random.uniform(1, 3)  # Turns ratio
    print(Fore.CYAN + f"Given a primary voltage of {primary_voltage} V and a turns ratio of {turns_ratio:.2f},")
    answer = get_float_input(Fore.GREEN + "What is the secondary voltage (V_s)? ")

    correct_answer = transformer_explanation(primary_voltage, turns_ratio)
    if abs(answer - correct_answer) < 0.01:
        print(Fore.GREEN + "Correct! Well done.")
        return True
    else:
        print(Fore.RED + f"Wrong! The correct answer is {correct_answer:.2f} V.")
        return False

def interactive_game():
    score = 0
    challenges = [
        ohms_law_challenge,
        power_calculation_challenge,
        series_resistance_challenge,
        parallel_resistance_challenge,
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
