from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import pyowm

root = Tk()
root.title("Weather App")
root.geometry("400x200")

def grapher():
    owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
    mgr = owm.weather_manager()
    place = e.get()
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    weather_list = forecast.weathers
    temp=[]
    time=[]
    for weather in weather_list:
        temp.append(int(weather.temperature(unit='celsius')['temp']))
        time.append(weather.reference_time('iso'))
    ypos = list(range(len(time)))
    plt.bar(ypos, temp)
    canvas = plt.show()
    canvas.show()
    canvas.get_tk_widget().grid(row=3,column=0)


Title = Label(root, text="Welcome to the Weather App!\n")
#Title.pack()

text = Label(root, text="Enter the name of the City:\n")
#text.pack()
e = Entry(root, width=20, borderwidth=5)
#e.pack()

Title.grid(row=0,column=0)
text.grid(row=1,column=0)
e.grid(row=1,column=2)

myButton = Button(root, text="Get Weather Forecast", command= grapher, padx=10, pady=5)
myButton.grid(row=3,column=2)



root.mainloop()
