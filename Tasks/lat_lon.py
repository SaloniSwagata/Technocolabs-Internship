import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
print("Enter the coordinates to find the weather")
lat=int(input("Enter the latitude: "))
lon=int(input("Enter the longitude: "))
obs = mgr.weather_at_coords(lat, lon)
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature at coordinates {lat}, {lon} is {temperature} degrees Fahrenheit.')
