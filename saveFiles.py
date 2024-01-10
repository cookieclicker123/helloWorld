from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/Users/seb/Desktop/helloWorld",
                                    defaultextension=".txt",
                                    filetypes= [
                                        ("Text files","*.txt"),
                                        ("HTML files","*.html"),
                                        ("All files","*.*")
                                    ]
                                    ) 

    if file is None:
        return
    
    filetext = input("Enter text to save:")
    #filetext = str(text.get("1.0",END))
    file.write(filetext) 
    file.close()

window = Tk()   

button = Button(window,text="save", command=saveFile)

button.pack()
text = Text(window)
text.pack() 

window.mainloop()