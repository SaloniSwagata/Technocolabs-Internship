from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import pyowm
import numpy as np

root = Tk()
root.title("Weather App")
root.geometry("400x200")



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

Title = Label(root, text="Welcome to the Weather App!\n")
#Title.pack()

text = Label(root, text="Enter the name of the City:\n")
#text.pack()
e = Entry(root, width=20, borderwidth=5)
#e.pack()

Title.grid(row=0,column=0)
text.grid(row=1,column=0)
e.grid(row=1,column=2)

myButton = Button(root, text="Get Weather Forecast in Bar Graph", command= bargraph, padx=10, pady=5)
myButton1 = Button(root, text="Get Weather Forecast in Line Graph", command= linegraph, padx=10, pady=5)
myButton.grid(row=3,column=2)
myButton1.grid(row=6,column=2)



root.mainloop()
