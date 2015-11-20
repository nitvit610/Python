import time
from tkinter import *

def window():

    timeClock = time.gmtime()

    timeFormat = (timeClock[3], ":", timeClock[4], ":", timeClock[5])
    
    global text

    text=Label(text=timeFormat)
    text.pack()

def refresher():
    global text
    text.configure(text=time.asctime() )
    root.after(1000, refresher) 

root=Tk()
window()
refresher()
root.mainloop()

