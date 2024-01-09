from tkinter import *
from PIL import ImageTk, Image
window = Tk()

count=0

def click():
    global count
    count+=1
    print(count)
    

img = Image.open("/Users/seb/Desktop/rollerCoaster.jpg")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

button = Button(window,
                text="Click me!",
                command=click,
                foreground="red",
                background="black",
                activeforeground="red",
                activebackground="black",
                font=('Comic Sans MS', 12),
                state=ACTIVE,
                image=img,
                compound="bottom")

button.pack()

window.mainloop()