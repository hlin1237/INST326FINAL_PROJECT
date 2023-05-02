import tkinter as tk
import random

board = [['', '', ''], ['', '', ''], ['', '', '']]
players = ['X', 'O']
current_player = None

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
  while True:
    try:
      row = int(input(f"{player}'s turn. Please enter row number (1-3): ")) - 1
      col = int(input(f"{player}'s turn. Please enter column number (1-3): ")) - 1
      if board[row][col] == '':
        board[row][col] = player
        break
      else:
        print("That spot is already taken. Please choose another spot.")
    except (ValueError, IndexError):
      print("Invalid input. Please enter a number between 1 and 3.")

def get_computer_move(board, player):
  """this function would generate a move for the computer player,
  using some AI algorithm to choose the best move based on the 
  current board state, if the player decide to play against the AI"""
  # simple strategy: choose a random empty spot on the board
  while True:
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] == '':
      board[row][col] = player
      break

def check_win(board):
    """ this function would check if either player has won the game
  by checking all possible win conditions (3 in a row horizontally,
  vertically, or diagonally)."""
    
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
        
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True
    
    return False

def check_tie(board):
    """this function would check if the game has ended in a tie 
  (i.e. all spots on the board are filled with no winner)."""
    for row in board:
        for val in row:
            if val == '':
                return False
    return True

def reset_board():
   """Set the board to the initial state after each game"""
   global board
   board = [['', '', ''], ['', '', ''], ['', '', '']]
   display_board(board)

def play_again():
    """Prompt the user if they want to play again and return a boolean value indicating their choice"""
    root = tk.Tk()
    root.title("Play Again?")
    
    def on_yes():
        root.destroy()
        return True
    
    def on_no():
        root.destroy()
        return False
    
    tk.Label(root, text="Do you want to play again?").pack()
    
    yes_button = tk.Button(root, text="Yes", command=on_yes)
    yes_button.pack(side="left", padx=10, pady=10)
    
    no_button = tk.Button(root, text="No", command=on_no)
    no_button.pack(side="right", padx=10, pady=10)
    
    root.mainloop()


def main():
    """Handle the main game loop, calling the other functions as necessary and checking for win/loss/tie conditions to end the game"""
    player = 'X'
    display_board(board)
    while True:
        get_player_move(board, player)
        display_board(board)
        if check_win(board):
            print(f"{player} wins!")
            if not play_again():
                break
            else:
                reset_board()
                continue
        elif check_tie(board):
            print("It's a tie!")
            if not play_again():
                break
            else:
                reset_board()
                continue
        player = 'O' if player == 'X' else 'X'
        if player == 'X':
            computer_move = get_computer_move(board, player)
            board[computer_move[0]][computer_move[1]] = player
            display_board(board)
            if check_win(board):
                print(f"{player} wins!")
                if not play_again():
                    break
                else:
                    reset_board()
                    continue
            elif check_tie(board):
                print("It's a tie!")
                if not play_again():
                    break
                else:
                    reset_board()
                    continue
            player = 'O'

