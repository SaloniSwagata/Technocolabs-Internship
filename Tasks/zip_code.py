import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
Zip, code = input("Enter the zip code and the country code").split()
obs = mgr.weather_at_zip_code(Zip, code)
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature for {Zip}, {code} is {temperature} degrees Fahrenheit.')
