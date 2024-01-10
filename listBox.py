


def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
    

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

from tkinter import *   



window = Tk()   

listbox = Listbox(window,
                bg="#f7ffde",
                fg="dark green", 
                font=("Constantia",35),
                width=12,
                selectmode=MULTIPLE
)
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    
    print("You have ordered: ")
    for index in food:
        print(index)
    
    #print(listbox.get(listbox.curselection()))

listbox.pack()


listbox.insert(1, "pizza",)
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()


submitButton = Button(window,text="Submit",command=submit,compound="bottom")

submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()