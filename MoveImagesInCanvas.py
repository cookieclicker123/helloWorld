from tkinter import Tk, Canvas
from PIL import Image, ImageTk

def moveUp(event):
    canvas.move(myImage,0,-10)

def moveDown(event):
    canvas.move(myImage,0,10)

def moveLeft(event):
    canvas.move(myImage,-10,0)

def moveRight(event):
    canvas.move(myImage,10,0)

window = Tk()
window.bind("<w>",moveUp)
window.bind("<s>",moveDown)
window.bind("<a>",moveLeft)
window.bind("<d>",moveRight)

canvas = Canvas(window, width=500, height=500)

# Open the image file
img = Image.open("raceCar.png")  # replace with your image file path
# Resize the image using resize() function
img = img.resize((100, 100))
# Convert the Image object to a PhotoImage object
img = ImageTk.PhotoImage(img)

myImage = canvas.create_image(20, 20, anchor='nw', image=img)
canvas.pack()

window.mainloop()