import tkinter as tk
import random
from tkinter import messagebox

def choose_country():
    countries = ["france", "germany", "italy", "spain", "canada"]
    return random.choice(countries)

def display_country(country, guessed_letters):
    display = ""
    for letter in country:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def make_guess():
    global attempts, guessed_letters, country_to_guess

    guess = guess_entry.get().lower()
    guess_entry.delete(0, 'end')

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showerror("Error", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        return

    guessed_letters.append(guess)

    if guess not in country_to_guess:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        if attempts == 0:
            messagebox.showinfo("Game Over", f"Out of attempts! The country was: {country_to_guess}.")
            window.destroy()

    display = display_country(country_to_guess, guessed_letters)
    country_label.config(text=f"Country: {display}")

    if "_" not in display:
        messagebox.showinfo("Congratulations", f"You guessed the country: {country_to_guess}.")
        window.destroy()

attempts = 6
guessed_letters = []
country_to_guess = choose_country()

window = tk.Tk()
window.title("Country Guessing Game")

attempts_label = tk.Label(window, text=f"Attempts left: {attempts}")
attempts_label.pack()

country_label = tk.Label(window, text=f"Country: {display_country(country_to_guess, guessed_letters)}")
country_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

guess_button = tk.Button(window, text="Guess", command=make_guess)
guess_button.pack()

window.mainloop()
