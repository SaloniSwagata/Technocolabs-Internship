from tkinter import *

root = Tk()
root.title("Weather App")

Title = Label(root, text="Welcome to the Weather App!\n")
#Title.pack()

text = Label(root, text="Enter the name of the City:\n")
#text.pack()
e = Entry(root, width=20, borderwidth=5)
#e.pack()

Title.grid(row=0,column=0)
text.grid(row=1,column=0)
e.grid(row=1,column=2)


def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.grid(row=1,column=4)

myButton = Button(root, text="Get Weather Forecast", command=myClick, padx=10, pady=5)
myButton.grid(row=3,column=2)



root.mainloop()
