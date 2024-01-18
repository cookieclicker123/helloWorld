from tkinter import *
from PIL import Image, ImageTk

def moveUp(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def moveDown(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def moveLeft(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def moveRight(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()   

window.geometry("500x500")

window.bind("<w>",moveUp)
window.bind("<s>",moveDown)
window.bind("<a>",moveLeft)
window.bind("<d>",moveRight)
window.bind("<Up>",moveUp)
window.bind("<Down>",moveDown)
window.bind("<Left>",moveLeft)
window.bind("<Right>",moveRight) 

img = Image.open("raceCar.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

label = Label(window, image=img,bg="grey")

label.place(x=0,y=0)


window.mainloop()