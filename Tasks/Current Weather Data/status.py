import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of the city: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
status = weather.status
detailed = weather.detailed_status
print(place)
print(f"Today's weather: {status}")
print(f"Today's detailed weather: {detailed}")
