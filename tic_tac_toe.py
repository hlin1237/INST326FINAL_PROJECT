
#function 1

import tkinter as tk

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

def display_board(board):
  """  this function would take a 3x3 list representing the
  tic-tac-toe board and print it out to the console in a user-friendly 
  format """
  root = tk.Tk()
    root.title("Board")
    for row in range(len(board)):
        for col in range(len(board[row])):
            label = tk.Label(root, text=board[row][col], font=("Arial", 24), width=3, height=1, borderwidth=1, relief="solid")
            label.grid(row=row, column=col)
    root.mainloop()

def get_player_move(board, player):
  """this function would prompt the user for their move,
  validate the input, and update the board with the move if it is valid。"""
  pass

def get_computer_move(board, player):
  """this function would generate a move for the computer player,
  using some AI algorithm to choose the best move based on the 
  current board state, if the player decide to play against the AI"""
  pass
  
def check_win(board):
  """ this function would check if either player has won the game
  by checking all possible win conditions (3 in a row horizontally,
  vertically, or diagonally)."""
  pass

def check_tie(board):
  """this function would check if the game has ended in a tie 
  (i.e. all spots on the board are filled with no winner)."""
  pass

def reset_board():
  """Set the board to the initial state after each game"""
   display_board(board)

def play_again():
  """this function would prompt the user if they want to 
  play again after the game has ended and return a boolean 
  value indicating their choice."""
  pass

def main():
  """this function would handle the main game loop,
  calling the other functions as necessary and checking
  for win/loss/tie conditions to end the game."""
  pass
