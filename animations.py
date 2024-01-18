from tkinter import *
from PIL import Image, ImageTk
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 10
yVelocity = 8

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

img = Image.open("UFO.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

img2 = Image.open("space.png")
img2 = img2.resize((500, 500))
img2 = ImageTk.PhotoImage(img2)

myImage2 = canvas.create_image(0, 0, anchor='nw', image=img2)


myImage = canvas.create_image(0, 0, anchor='nw', image=img)

imageWidth = img.width()
imageHeight = img.height()


while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)
    if (coordinates[0] >= (WIDTH - imageWidth) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT - imageHeight) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(myImage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
    

window.mainloop()
