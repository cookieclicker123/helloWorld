from tkinter import *
from PIL import ImageTk, Image

window = Tk()

# Open the image file
img = Image.open("/Users/seb/Desktop/rollerCoaster.jpg")
# Resize the image
img = img.resize((200, 200))
# Convert the image to a Tkinter-compatible photo image
img = ImageTk.PhotoImage(img)

label = Label(window, 
            text="bro do you even code?",
            font=("Arial Bold",50),
            fg="#00ff00",bg="black",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=img,
            compound="top")

label.pack()

window.mainloop()
