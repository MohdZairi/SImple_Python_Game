import random
import tkinter as tk
from tkinter import messagebox

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Create a tkinter window
window = tk.Tk()
window.title("Guessing Game")

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess == secret_number:
            result = f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts."
            messagebox.showinfo("Result", result)
            window.quit()
        elif guess < secret_number:
            result_label.config(text="Try a higher number.")
        else:
            result_label.config(text="Try a lower number.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

prompt_label = tk.Label(window, text="Enter your guess: ")
entry = tk.Entry(window)
check_button = tk.Button(window, text="Check", command=check_guess)
result_label = tk.Label(window, text="")

prompt_label.pack()
entry.pack()
check_button.pack()
result_label.pack()

window.mainloop()

# End of the game
print("Thank you for playing!")
