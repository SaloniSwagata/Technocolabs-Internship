import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
Id = int(input("Enter the city id: "))
obs = mgr.weather_at_id(Id)
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature for city id {Id} is {temperature} degrees Fahrenheit.')
