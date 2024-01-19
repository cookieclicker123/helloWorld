import os
from tkinter import *
from tkinter import StringVar
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *    
from tkinter.filedialog import *


def changeColour():
    colour = colorchooser.askcolor(title="Choose Colour")
    textArea.config(fg=colour[1])

def changeFont(*args):
    textArea.config(font=(fontName.get(),fontSize.get()))


def newFile():
    window.title("Unititled - Text Editor Program")
    textArea.delete(1.0,END)

def openFile():
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    try:
        window.title(os.path.basename(file) + " - Text Editor Program")
        textArea.delete(1.0,END)
        file = open(file,"r")
        textArea.insert(1.0,file.read())
    except FileNotFoundError:
        print("Cannot open file")
    finally:
        file.close()


def saveFile():
    file = filedialog.asksaveasfile(mode='w', initialfile='Untitled.txt',
                                    defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if file is not None:
        data = textArea.get(1.0, END)
        file.write(data)
        file.close()
        window.title(os.path.basename(file.name) + " - Text Editor Program")
    else:
        print("Save operation cancelled")

def cut():
    textArea.event_generate("<<Cut>>")  

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    showinfo("About this program","This is a text editor program")

def quitApp():
    window.destroy()

window = Tk()   

window.title("Text Editor Program")

file = None

windowWidth = 500
windowHeight = 500
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,x,y))

fontName = StringVar(window)
fontName.set("Arial")
fontSize = StringVar(window)
fontSize.set("25")

textArea = Text(window,font=(fontName.get(),fontSize.get()))

scrollBar = Scrollbar(textArea)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
textArea.grid(sticky=N+E+S+W)
scrollBar.pack(side=RIGHT,fill=Y)
textArea.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=textArea.yview)

frame = Frame(window)
frame.grid()    

colourButton = Button(frame,text="Colour",command=changeColour)
colourButton.grid(row=0,column=0)

fontBox = OptionMenu(frame,fontName,*font.families(),command=changeFont)
fontBox.grid(row=0,column=1)

fontSizeBox = Spinbox(frame,from_= 1,to = 100,textvariable=fontSize,command=changeFont)
fontSizeBox.grid(row=0,column=2)

menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar)
menuBar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)

editMenu = Menu(menuBar)
menuBar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="About",command=about)







window.mainloop()



