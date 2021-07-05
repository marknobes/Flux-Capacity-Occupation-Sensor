from tkinter import *

#initializes tkinter to be able to create the program ui
root = Tk()

def Onclickstart():
    label1 = Label(root, text = "placeholder for start") #creation of label
    label1.pack #puts label on the window

Title = Label(root, text = "Flux Capacity Occupation Sensor")
Title.pack()
startbutton = Button(root, text = "Start", command=Onclickstart)
startbutton.pack

root.mainloop()
