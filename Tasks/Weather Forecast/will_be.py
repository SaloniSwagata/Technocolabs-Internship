import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place= input("Enter the name of your city: ")
forecaster = mgr.forecast_at_place(place, '3h')

print("Stormy: " + str(forecaster.will_be_stormy_at(timestamps.tomorrow(15,0))))
print("Foggy: " + str(forecaster.will_be_stormy_at(timestamps.tomorrow(12,0))))
print("Clear-Sky: " + str(forecaster.will_be_stormy_at(timestamps.tomorrow(8,30))))
