import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of the city: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
humidity = weather.humidity
print(f'The current humidity for {place} is {humidity}%')
clouds = weather.clouds
print(f'The current cloud coverage for {place} is {clouds}%')
speed = weather.wind(unit = 'miles_hour')['speed']
print(f'The current wind speed for {place} is {speed}mph')
