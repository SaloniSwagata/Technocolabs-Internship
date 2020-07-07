from tkinter import *

root = Tk()
root.title("Weather App")

myLabel = Label(root, text="Welcome to the Weather App!")
myLabel.pack()

e = Entry(root, width=35, borderwidth=5)
e.pack()
