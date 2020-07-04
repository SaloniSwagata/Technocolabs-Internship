import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature in San Francisco, California is {temperature} degrees Fahrenheit.')
