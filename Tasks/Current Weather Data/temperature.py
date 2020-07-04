import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of a city: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
tempf = weather.temperature(unit='fahrenheit')['temp']
tempc = weather.temperature(unit='celsius')['temp']
print(f"The temperature in {place} is {tempf} in Farenheit and {tempc} in Celsius")
