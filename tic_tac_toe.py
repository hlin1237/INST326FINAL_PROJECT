from tkinter import *

def next_turn(row, col):
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
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] !="":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True 
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True 
    elif check_tie() is False:
        return "Tie"
    else:
        return False

def check_tie():
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
    global player
    player = "x"
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
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

def board():
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


    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text ="",
            font = ('consolas', 40), width=5, height = 2, command = lambda row=row, column=column: next_turn(row, column) )

            buttons[row][column].grid(row=row, column=column)

    # go find out what this mean later
    window.mainloop()




if __name__ == '__main__':
    board()
