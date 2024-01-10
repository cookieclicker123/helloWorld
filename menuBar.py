from tkinter import *
from PIL import ImageTk,Image



def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():    
    print("You pasted some text")

window = Tk()

openImage = Image.open("/Users/seb/Desktop/open.png")
openImage = openImage.resize((65,65))
openImage = ImageTk.PhotoImage(openImage)

saveImage = Image.open("/Users/seb/Desktop/save.png")
saveImage = saveImage.resize((65,65))
saveImage = ImageTk.PhotoImage(saveImage)

exitImage = Image.open("/Users/seb/Desktop/exit.png")
exitImage = exitImage.resize((65,65))
exitImage = ImageTk.PhotoImage(exitImage)




menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar)
menuBar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)

editMenu = Menu(menuBar)
menuBar.add_cascade(label="Edit",menu=editMenu) 
editMenu.add_command(label="Cut",command=cut)
editMenu.add_separator()
editMenu.add_command(label="Copy",command=copy)
editMenu.add_separator()
editMenu.add_command(label="Paste",command=paste)

window.mainloop()