import random
import tkinter as tk
from tkinter import messagebox

# Define the options
options = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player_choice):
    computer_choice = random.choice(options)
    result = ""

    if player_choice not in options:
        result = "Invalid choice. Please choose rock, paper, or scissors."
    else:
        result = f"Computer's choice: {computer_choice}\nYour choice: {player_choice}\n"

        if player_choice == computer_choice:
            result += "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            result += "You win!"
        else:
            result += "Computer wins!"

    messagebox.showinfo("Result", result)

# Create a tkinter window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Function to make a choice
def make_choice(player_choice):
    determine_winner(player_choice)

# Add buttons for player's choices
rock_button = tk.Button(window, text="Rock", command=lambda: make_choice("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: make_choice("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: make_choice("scissors"))

rock_button.pack(side="left")
paper_button.pack(side="left")
scissors_button.pack(side="left")

# Start the tkinter main loop
window.mainloop()
