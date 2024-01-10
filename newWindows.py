from tkinter import *

def createWindow():
    newWindow = Tk()
    oldWindow.destroy()

oldWindow = Tk()   

Button(oldWindow,text="create new window", command=createWindow).pack()


oldWindow.mainloop()   