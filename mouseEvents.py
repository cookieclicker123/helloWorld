from tkinter import *

def doSomething(event):
    print("Mouse coordinates" +str(event.x) + "," + str(event.y))

window = Tk()   

#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel click
#window.bind("<Button-3>",doSomething)
#window.bind("<ButtonRelease>",doSomething) #release mouse button
#window.bind("<Enter>",doSomething) #mouse enters widget
#window.bind("<Leave>",doSomething) #mouse leaves widget\
window.bind("<Motion>",doSomething) #mouse moves within widget



window.mainloop()