from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import pyowm
import numpy as np
from tabulate import tabulate


root = Tk()
root.title("Weather App")
root.config(bg="skyblue")

def display(time,Min,Max):
    place = e.get()
    print(f"The 5 day forecast for {place} is as follows - ")
    print()
  
    i=0
    l=[]
    for i in range(len(time)):
        l.append([time[i],Min[i],Max[i]])
    table = tabulate(l, headers=['Day', 'Minimum Temperature', 'Maximum Temperature'], tablefmt='orgtbl')

    print(table)

def bargraph():
    owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
    degree_sign= u'\N{DEGREE SIGN}'
    mgr = owm.weather_manager()
    place = e.get()
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    weather_list = forecast.weathers
    temp_min=[]
    temp_max=[]
    time=[]
    date=0
    t_min=[]
    t_max=[]
    for weather in weather_list:
        d=(weather.reference_time('iso').split(" "))[0]
        if d!=date:
            date=d
            if t_min!=[]:
                total1=min(t_min)
                total2=max(t_max)
                temp_min.append(total1)
                temp_max.append(total2)
                time.append(d.split("-")[2]+"/"+d.split("-")[1])
            t_min=[]
            t_max=[]
            t_min.append(int(weather.temperature(unit='celsius')['temp_min']))
            t_max.append(int(weather.temperature(unit='celsius')['temp_max']))
        else:
            t_min.append(int(weather.temperature(unit='celsius')['temp_min']))
            t_max.append(int(weather.temperature(unit='celsius')['temp_max']))
        
    xpos = np.arange(len(time))
    fig, ax = plt.subplots()
    bar_width = 0.35
    barMin = ax.bar(xpos-bar_width/2,temp_min , bar_width, label="Minimum Temperature")
    barMax = ax.bar(xpos+bar_width/2,temp_max , bar_width, label="Maximum Temperature")
    
    display(time,temp_min,temp_max)

    # inserting x axis label
    ax.set_xticks(xpos)
    ax.set_xticklabels(xpos)

    # inserting y axis label
    ax.set_yticks(np.arange(0, 100, 10))
    ax.set_yticklabels(np.arange(0, 100, 10))
    plt.xticks(xpos,time)
    plt.title(f'Weather Forecast For {place}')
    plt.ylabel(f"Temperature ({degree_sign}C)")
    plt.xlabel("Day")

    """Attach a text label above each bar in *rects*, displaying its height."""

    for rect in barMin:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    for rect in barMax:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    plt.legend()
    canvas = plt.show()
    #canvas.show()
    #canvas.get_tk_widget().grid(row=3,column=0)


def linegraph():
    owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
    degree_sign= u'\N{DEGREE SIGN}'
    mgr = owm.weather_manager()
    place = e.get()
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    weather_list = forecast.weathers
    temp_min=[]
    temp_max=[]
    time=[]
    date=0
    t_min=[]
    t_max=[]
    for weather in weather_list:
        d=(weather.reference_time('iso').split(" "))[0]
        if d!=date:
            date=d
            if t_min!=[]:
                total1=min(t_min)
                total2=max(t_max)
                temp_min.append(total1)
                temp_max.append(total2)
                time.append(d.split("-")[2]+"/"+d.split("-")[1])
            t_min=[]
            t_max=[]
            t_min.append(int(weather.temperature(unit='celsius')['temp_min']))
            t_max.append(int(weather.temperature(unit='celsius')['temp_max']))
        else:
            t_min.append(int(weather.temperature(unit='celsius')['temp_min']))
            t_max.append(int(weather.temperature(unit='celsius')['temp_max']))

    display(time,temp_min,temp_max)

    xpos = np.arange(len(time))    
    plt.plot(xpos, temp_min , color='blue', label="Minimum Temperature")
    plt.plot(xpos, temp_max, color='orange', label="Maximum Temperature")
    plt.title(f'Weather Forecast For {place}')
    plt.ylabel(f"Temperature ({degree_sign}C)")
    plt.xlabel("Day")
    plt.xticks(xpos,time)
    plt.yticks(np.arange(0, 100, 10))

    # zip joins x and y coordinates in pairs
    for x,y in zip(xpos,temp_min):
        label = "{}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

    # zip joins x and y coordinates in pairs
    for x,y in zip(xpos,temp_max):
        label = "{}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center


    
    plt.legend()
    canvas = plt.show()


Title = Label(root, text="Welcome to the Weather App!", bg="skyblue", fg="white", font="none 28 bold")
Title.config(anchor=CENTER)

text = Label(root, text="Enter the name of the City:", bg="skyblue", fg="black", font="none 20 bold")
e = Entry(root, width=10, font=('Helvetica', 30))
#e.pack()

Title.grid(row=1,column=0, padx=5, pady=5)
text.grid(row=2,column=0)
e.grid(row=2,column=1)

myButton = Button(root, text="Get Weather Forecast in Bar Graph", command= bargraph, padx=10, pady=5)
myButton1 = Button(root, text="Get Weather Forecast in Line Graph", command= linegraph, padx=10, pady=5)
myButton.grid(row=3,column=0, pady=10)
myButton1.grid(row=4,column=0, pady=10)



root.mainloop()
