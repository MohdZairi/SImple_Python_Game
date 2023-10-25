import tkinter as tk
from tkinter import messagebox
import random

def generate_sequence():
    return [random.randint(1, 9) for _ in range(5)]

def start_game():
    global sequence, player_sequence, game_round
    sequence = generate_sequence()
    player_sequence = []
    game_round = 1
    show_sequence()

def show_sequence():
    info_label.config(text=f"Round {game_round}: Remember the sequence.")
    window.after(2000, show_blank)

def show_blank():
    info_label.config(text="Now, enter the numbers.")
    input_entry.config(state=tk.NORMAL)
    confirm_button.config(state=tk.NORMAL)
    input_entry.delete(0, tk.END)
    window.after(4000, check_sequence)

def check_sequence():
    player_input = input_entry.get()
    input_entry.delete(0, tk.END)
    player_sequence.append(int(player_input))

    if player_sequence == sequence:
        info_label.config(text="Correct! Next round.")
        input_entry.config(state=tk.DISABLED)
        confirm_button.config(state=tk.DISABLED)
        window.after(2000, start_game)
    else:
        info_label.config(text="Incorrect. Game over!")
        input_entry.config(state=tk.DISABLED)
        confirm_button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", f"Your score: {game_round - 1}")

window = tk.Tk()
window.title("Number Memory Game")

info_label = tk.Label(window, text="Click 'Start' to begin.")
info_label.pack()

start_button = tk.Button(window, text="Start", command=start_game)
start_button.pack()

input_entry = tk.Entry(window, state=tk.DISABLED)
input_entry.pack()

confirm_button = tk.Button(window, text="Confirm", command=check_sequence, state=tk.DISABLED)
confirm_button.pack()

window.mainloop()
