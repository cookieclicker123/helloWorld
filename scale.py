from tkinter import *

from PIL import ImageTk, Image


def submit():
    print("The temperature is: {} Degrees Celsius".format(scale.get()))

window = Tk()

hotImg = Image.open("/Users/seb/Desktop/hot.jpg")


hotImg = hotImg.resize((100, 100))


hotImg = ImageTk.PhotoImage(hotImg)


hotLabel = Label(image=hotImg) 
hotLabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Impact", 20),
              tickinterval=10,
              showvalue=0,
              resolution=10,
              troughcolor="light blue",
              fg="red",
              bg="black",
              )

scale.set(((scale['from']- scale['to'])/2)+scale['to'])
button = Button(window,text="submit",command=submit)
button.pack()

scale.pack()

coldImg = Image.open("/Users/seb/Desktop/cold.jpg")

coldImg = coldImg.resize((100, 100))

coldImg = ImageTk.PhotoImage(coldImg)

coldLabel = Label(image=coldImg)
coldLabel.pack()

window.mainloop()
