from tkinter import *
from tkinter import messagebox


def click():
    #messagebox.showinfo(title="This is an info message box",message="You are awesome!")
    #messagebox.showwarning(title="This is a warning message box",message="You have a virus!")
    #messagebox.showerror(title="This is an error message box",message="Something went wrong!")
    #if messagebox.askokcancel(title="ask ok cancel",message="Are you sure you want to do this?"):
     #   print("You did a thing")
    #else:
     #   print("You cancelled the thing")
    #if messagebox.askretrycancel(title="ask retry cancel",message="Do you want to retry that again?"):
     #   print("You retried the thing")
    #else:
     #   print("You cancelled the thing")
    #if messagebox.askyesno(title="ask yes no",message="Do you like pie?"):
     #   print("i like pie too")
    #else:
    #    print("You don't like pie")
    #answer = messagebox.askquestion(title="ask question",message="Do you like pie?")
    #if answer == "yes":
     #   print("i like pie too")
    #else:
     #   print("You don't like pie")
    answer = messagebox.askyesnocancel(title="yes no cancel",message="Do you like to code?",icon="warning")
    if answer == True:
        print("You like to code")
    elif answer == False:
        print("You don't like to code")
    else:
        print("You cancelled the thing")


window = Tk()

button = Button(window,command=click,text="Click me")
button.pack()


window.mainloop()