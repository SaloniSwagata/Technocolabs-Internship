import pyowm
import pytz
from datetime import datetime

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of the city: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
sunrise = weather.sunrise_time()
sunset = weather.sunset_time(timeformat='iso')
print(f"The time for sunrise and sunset in {place} in unix and iso is: {sunrise}, {sunset}")

