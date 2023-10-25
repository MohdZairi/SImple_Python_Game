import tkinter as tk
from tkinter import messagebox
import random

# Create a function to check for a win
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Create a function for a button click
def on_click(row, col):
    global player, winner

    if board[row][col] == " " and not winner:
        board[row][col] = player
        buttons[row][col].config(text=player)
        if check_winner(board, player):
            winner = player
            messagebox.showinfo("Game Over", f"Player {player} wins!")
        elif all(cell != " " for row in board for cell in row):
            winner = "Tie"
            messagebox.showinfo("Game Over", "It's a tie!")
        player = "X" if player == "O" else "O"
        if player == "O" and not winner:
            computer_move()

# Create a function for the computer's move
def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        on_click(row, col)

# Create the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

# Create the buttons for the board
buttons = [[None, None, None] for _ in range(3)]

# Create buttons for the board
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Initialize the game
player = "X"
winner = None

# Run the main game loop
root.mainloop()
