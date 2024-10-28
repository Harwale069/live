import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Electrical Engineering Interactive Game")
root.geometry("600x400")
root.configure(bg="#f0f0f5")

# Global score counter
score = 0

# Sample Questions and Answers
questions = [
    {
        "question": "What is the total resistance (R_total) for R1 = 5 Ω and R2 = 3 Ω in series?",
        "answer": 8,
        "hint": "In series circuits, resistances add up."
    },
    {
        "question": "What is the secondary voltage (V_s) for a primary voltage of 131 V and turns ratio of 1.57?",
        "answer": 206.04,
        "hint": "Use V_secondary = V_primary * turns ratio."
    }
]

# Function to check answer
def check_answer(question_idx):
    global score
    user_answer = entry.get()
    try:
        if float(user_answer) == questions[question_idx]["answer"]:
            score += 1
            messagebox.showinfo("Correct!", "Well done! Correct answer.")
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer was {questions[question_idx]['answer']}.")
        next_question()
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a numeric value.")

# Function to display next question
def next_question():
    global question_idx
    question_idx += 1
    if question_idx < len(questions):
        question_label.config(text=questions[question_idx]["question"])
        entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Game Over", f"Final Score: {score}/{len(questions)}")
        root.destroy()

# Function to show hint
def show_hint():
    messagebox.showinfo("Hint", questions[question_idx]["hint"])

# Calculator function
def calculator():
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculator")
    calc_entry = tk.Entry(calc_window, width=20, font=("Arial", 14))
    calc_entry.pack(pady=10)

    def calculate():
        try:
            result = eval(calc_entry.get())
            messagebox.showinfo("Result", f"Result: {result}")
        except:
            messagebox.showerror("Error", "Invalid expression")

    calc_button = tk.Button(calc_window, text="Calculate", command=calculate)
    calc_button.pack(pady=10)

# Main UI elements
question_idx = 0
question_label = tk.Label(root, text=questions[question_idx]["question"], font=("Arial", 14), bg="#f0f0f5", wraplength=500)
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), width=10)
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f5")
button_frame.pack(pady=20)

check_button = tk.Button(button_frame, text="Submit Answer", command=lambda: check_answer(question_idx))
check_button.grid(row=0, column=0, padx=5)

hint_button = tk.Button(button_frame, text="Hint", command=show_hint)
hint_button.grid(row=0, column=1, padx=5)

calc_button = tk.Button(button_frame, text="Calculator", command=calculator)
calc_button.grid(row=0, column=2, padx=5)

# Start with the first question
question_idx = 0
next_question()

# Run the main loop
root.mainloop()
