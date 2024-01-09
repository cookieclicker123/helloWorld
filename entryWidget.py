from tkinter import *

def submit():
    username = entry.get()
    print("Username: " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backSpace():
    entry.delete(len(entry.get())-1, END)   

window = Tk()

entry = Entry(window,
              font=("Arial Bold", 50),
              fg="#00ff00",
              bg="black",
              show="*",
                    )

entry.insert(0, "Enter: ")
entry.pack(side=LEFT)

submitButton = Button(window,text="Submit", command=submit)
submitButton.pack(side=RIGHT)

deleteButton = Button(window,text="delete", command=delete)
deleteButton.pack(side=RIGHT)

backSpaceButton = Button(window,text="backspace", command=backSpace)
backSpaceButton.pack(side=RIGHT)

window.mainloop()