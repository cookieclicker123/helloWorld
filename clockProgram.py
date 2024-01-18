from tkinter import *
import time

def update():
    time_string = time.strftime("%I:%M:%S %p")  
    timeLabel.config(text=time_string)

    day_string = time.strftime("%A")
    dayLabel.config(text=day_string)

    date_string = time.strftime("%B %d, %Y")
    dateLabel.config(text=date_string)
    
    window.after(1000, update)

window = Tk()   

timeLabel = Label(window,font=("Arial", 50), fg="green",bg="black")
timeLabel.pack()

dayLabel = Label(window,font=("Ink Free", 25))
dayLabel.pack()

dateLabel = Label(window,font=("Ink Free", 25))
dateLabel.pack()

update()


window.mainloop()