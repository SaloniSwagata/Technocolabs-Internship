import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of the place: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature at {place} is {temperature} degrees Fahrenheit.')
