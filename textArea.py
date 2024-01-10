from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,bg="light yellow",fg="dark blue",font=("ink free",25),height=8,width=20,padx=20,pady=20
)
text.pack()
button = Button(window,command=submit,text="Submit")
button.pack()

window.mainloop()