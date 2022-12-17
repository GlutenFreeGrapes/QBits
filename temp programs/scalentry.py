#Import the Tkinter Library
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Create an Integer Variable to set the initial value of Scale
var = IntVar()

#Create an Entry widget
entry = Entry(win,width= 4,textvariable=var)
scale = Scale(win, from_=0, to=500, length= 400, orient="horizontal", variable=var)
scale.set(250)
entry.place(relx= .5, rely= .5, anchor= CENTER)
scale.place(relx= .5, rely= .6, anchor = CENTER)

win.mainloop()