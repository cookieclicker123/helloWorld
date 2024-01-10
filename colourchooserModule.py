from tkinter import *
from tkinter import colorchooser

def click():
    colour = colorchooser.askcolor()
    print(colour)
    colourHex = colour[1]
    print(colourHex)
    window.config(bg=colourHex)

window = Tk()

window.geometry("420x420")
button = Button(text="Click me",command=click)
button.pack()

window.mainloop()