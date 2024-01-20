from tkinter import *
import random

def nextTurn(row, column):
    global player
    if buttons[row][column]["text"] == " " and not checkWin():
        buttons[row][column]["text"] = player
        if checkWin():
            label.config(text=(player + " wins"))
            disableAllButtons()
        elif emptySpaces() is False:
            label.config(text="Tie")
            highlightAllButtons("red")
            disableAllButtons()
        else:
            player = players[0] if player == players[1] else players[1]
            label.config(text=player + " turn")

def checkWin():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != " ":
            for button in buttons[row]:
                button.config(background="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != " ":
            for row in range(3):
                buttons[row][column].config(background="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
        for i in range(3):
            buttons[i][i].config(background="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
        for i in range(3):
            buttons[i][2-i].config(background="green")
        return True
    return False

def highlightAllButtons(color):
    for row in buttons:
        for button in row:
            button.config(background=color)

def disableAllButtons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def emptySpaces():
    spaces = [button["text"] == " " for row in buttons for button in row]
    return any(spaces)

def newGame():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in buttons:
        for button in row:
            button.config(text=" ", bg="SystemButtonFace", state=NORMAL)

window = Tk()
window.title("Tic Tac Toe Game")
players = ["X", "O"]
player = random.choice(players)
label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

resetButton = Button(text="Restart", font=("consolas", 20), command=newGame)
resetButton.pack(side="top")

frame = Frame(window)
frame.pack()

buttons = [[None, None, None] for _ in range(3)]
for row in range(3):
    for column in range(3):
        button = Button(frame, text=" ", font=("consolas", 40), width=5, height=2,
                        command=lambda row=row, column=column: nextTurn(row, column))
        button.grid(row=row, column=column)
        buttons[row][column] = button

window.geometry("500x500")
window.mainloop()