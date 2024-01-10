from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/Users/seb/Desktop/helloWorld",
                                          title="Open file okay?",
                                          filetypes=(("text files","*.txt"),
                                                     ("all files","*.*"))
                                          )
    
    
    file = open(filepath,"r")
    print(file.read())
    file.close()
        

window = Tk()

button = Button(text="open",command=openFile)
button.pack()

window.mainloop()