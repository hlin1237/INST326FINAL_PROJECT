from tkinter import *
from tkinter import messagebox
import webbrowser

def next_turn(row, col):
    """ 
        Arg:
            row (int): row number of the button clicked
            col (int): column number of the button clicked
        purpose:
            Determine the next player's tun and updates the game board accordingly
        Negative impact: 
            None
    """
    global player
    if buttons[row][col]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[1]
                
                ai_play()
            elif check_winner() is True:
                label.config(text = (players[0] + " wins"))
                label.pack(side ="top")
            elif check_winner() == "Tie":
                label.config(text = "Tie")
                label.pack(side ="top")
            else:
            
                label.config(text = "Tie")
                label.pack(side ="top")

def check_winner():
    """
    Checks if there is a winner in the Tic Tac Toe game

    This function checks if there is a winner by examining the values of the text attribute of the buttons in the Tic Tac Toe game board

    Returns:
        bool or str: Returns True if there is a winner, "Tie" if the game is tied, and False otherwise
    """
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] !="":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
          buttons[0][0].config(bg="green")
          buttons[1][1].config(bg="green")
          buttons[2][2].config(bg="green")
          return True 
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
         buttons[0][2].config(bg="green")
         buttons[1][1].config(bg="green")
         buttons[2][0].config(bg="green")
         return True 
    elif check_tie() is False:
        return "Tie"
    else:
        return False

def check_tie():
    """Check if the Tic Tac Toe game is tied.

    This function checks if the Tic Tac Toe game board is full and there is no winner. 
    If there are no more empty spaces on the board and there is no winner, the function returns False.
    Otherwise, it returns True

    Returns:
        bool: Returns False if the game is tied, and True otherwise
    """
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    """
        Arg: None
        Purpose: This function helps reset a new game state for the tic tac toe board.
                 The for loop in this function is what is used to reset the buttons on the interface.
    
    """
    
    global player
    player = "x"
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="",bg ="#F0F0F0")
            buttons[row][col].config(state="normal")

def ai_play():
    global player
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                buttons[row][col]["text"] = player
                buttons[row][col].config(state="disabled")
                if check_winner() is False:
                    player = players[0]
                elif check_winner() is True:
                    label.config(text=(players[1] + " wins"))
                    label.pack(side ="top")
                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    label.pack(side ="top")
                return
def make_buttons(frame):
    """
        Arg:
            Frame '(tkinter Frame): Frame where the buttons will be placed
        Purposes:
            Creates the 3 x 3 grid of buttons for the game board 
            
    """
    
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text ="",
            font = ('consolas', 40), width=5, height = 2, command = lambda row=row, column=column: next_turn(row, column) )

            buttons[row][column].grid(row=row, column=column)
            
def instruction():
    """
        Arg: 
            none
        Purpose: Creates a popup button with instructions for users on how to operate this tic tac toe game.
                 There is also a video link if you click yes to add further help for a user on playing tic tac toe. 
    
    """
    
    message = "Welcome to Tic-Tac-Toe!\n\n"
    message += "The game is played on a 3x3 grid. You will play as 'X' and the AI will play as 'ai'. "
    message += "The goal is to get three of your symbols in a row, column, or diagonal.\n\n"
    message += "Pay attention to the AI's moves. It will try to anticipate your strategy and block your winning moves.\n\n"
    message += "Think strategically and plan your moves carefully. Consider different possibilities and potential winning patterns.\n\n"
    message += "Remember, the key to winning is to think ahead and outsmart the AI.\n\n"
    message += "(If you still have trouble understanding how to play Tic-Tac-Toe click yes and more instruction will be given.) \n\n"
    message += "Enjoy playing Tic-Tac-Toe and may the best strategist win!"
    def callback(event):
        webbrowser.open_new("https://www.youtube.com/watch?v=3qzcAMShotQ")

    root = Tk()
    root.withdraw()
    result = messagebox.askquestion("Instructions", message, icon='info')

    if result == 'yes':
        webbrowser.open('https://www.youtube.com/watch?v=3qzcAMShotQ')
            
def board():
    """ 
    Arg:
            None
        Purpose: 
            Initializes the game board and starts the game 
    
    """
    
    global players, player, buttons, label
    window = Tk()
    window.title("Tic-Tac-Toe")

    players = ["x", "ai"]
    player = "x"

    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    label = Label(text = "Tic-Tac-Toe", font = ('consolas', 40))
    label.pack(side ="top")
    reset_button = Button(text="restart", font = ('consolas', 20), command =new_game)
    reset_button.pack(side = "top")
    
    instruction_button = Button(text="instruction", font = ('consolas', 10), command = instruction)
    instruction_button.pack(side="top", anchor="ne")
    frame = Frame(window)
    frame.pack()
    


    frame = Frame(window)
    frame.pack()
    
    
    make_buttons(frame)

  
    window.mainloop()




if __name__ == '__main__':
    board()
