from tkinter import *   
from PIL import ImageTk, Image


def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You don't agree")

window = Tk() 


img = Image.open("/Users/seb/Desktop/Python.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

x = IntVar()

        
checkButton = Checkbutton(window, 
                          text = "Check Button",
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command=display,
                          font=("Arial Bold", 20),
                          fg="#00FF00",
                          bg="Black",
                          padx=50,
                          pady=10,
                          image=img,
                          compound="left",
                          )

checkButton.pack()

window.mainloop()