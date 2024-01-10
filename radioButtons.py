from tkinter import *
from PIL import ImageTk, Image

food = ["Pizza", "Hamburger", "Hot Dog"]

def order():
    if x.get() == 0:
        print("You ordered a pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hot dog")
    else:
        print("You didn't order anything")

window = Tk()

pizzaImg = Image.open("/Users/seb/Desktop/pizza.png")
hamImg = Image.open("/Users/seb/Desktop/hamburger.png") 
hotDogImg = Image.open("/Users/seb/Desktop/hotdog.png")

pizzaImg = pizzaImg.resize((100, 100))
hamImg = hamImg.resize((100, 100))
hotDogImg = hotDogImg.resize((100, 100))

pizzaImg = ImageTk.PhotoImage(pizzaImg)
hamImg = ImageTk.PhotoImage(hamImg)
hotDogImg = ImageTk.PhotoImage(hotDogImg)

foodImages = [pizzaImg, hamImg, hotDogImg]



x = IntVar()    

for index in range (len(food)):
    radioButton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radio buttons together if they share the same variable
                              value=index,#assigns each radio button a different value
                              fg="red",
                              bg="Black",  
                              padx=25,
                              font=("impact",50),
                              image=foodImages[index],#adds images to radio buttons
                              compound="left",
                              indicatoron=0,#removes the circle indicator
                              width=375,
                              command=order  

                            

     ) 
    
    radioButton.pack(anchor=W)
                          

window.mainloop()
