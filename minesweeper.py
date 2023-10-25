import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_locations = set()

    while len(mine_locations) < mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        mine_locations.add((row, col))
        board[row][col] = 'M'

    return board

def load_image(file_path):
    image = Image.open(file_path)
    image = image.resize((40, 40))
    return ImageTk.PhotoImage(image)

def on_click(row, col):
    if board[row][col] == 'M':
        display_explosion(row, col)
        game_over_label.config(text="Game Over!")
        disable_all_buttons()
    else:
        reveal_square(row, col)

def display_explosion(row, col):
    explosion_image = load_image("image/bom.jpeg")  # Load the explosion image
    buttons[row][col].config(image=explosion_image, text="")

def reveal_square(row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True
    buttons[row][col].config(state=tk.DISABLED)

    if board[row][col] == 'M':
        return

    adjacent_mines = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'M':
                adjacent_mines += 1

    if adjacent_mines > 0:
        buttons[row][col].config(text=str(adjacent_mines))
    else:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and not revealed[r][c]:
                    reveal_square(r, c)

    if all(all(revealed[i][j] or board[i][j] == 'M' for j in range(cols)) for i in range(rows)):
        game_over_label.config(text="Congratulations! You've won!")

def disable_all_buttons():
    for i in range(rows):
        for j in range(cols):
            buttons[i][j].config(state=tk.DISABLED)

# Create the game window
window = tk.Tk()
window.title("Minesweeper")

# Set board size and number of mines
rows, cols, mines = 8, 8, 10

board = initialize_board(rows, cols, mines)
revealed = [[False for _ in range(cols)] for _ in range(rows)]

mine_image = load_image("image/bom.jpeg")
explosion_image = load_image("image/bom.jpeg")

buttons = []
for i in range(rows):
    row_buttons = []
    for j in range(cols):
        button = tk.Button(window, image=None, text=" ", width=4, height=2, command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

game_over_label = tk.Label(window, text="", font=("Helvetica", 16))
game_over_label.grid(row=rows, columnspan=cols)

window.mainloop()
