from tkinter import *
from tkinter.ttk import *

def start():
    increment_progress_bar(0)


def increment_progress_bar(download):
    GB = 100
    speed = 1
    if download <= GB:
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+"GB completed")
        bar['value'] = (download/GB)*100
        window.after(50, lambda: increment_progress_bar(download+speed))

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()


button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()