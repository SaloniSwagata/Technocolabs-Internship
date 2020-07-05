import pyowm

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')
mgr = owm.weather_manager()
place = input("Enter the name of the city: ")
forecaster = mgr.forecast_at_place(place, '3h')

print("Rains: "+str(forecaster.will_have_rain()))
print("Clouds: "+str(forecaster.will_have_clouds()))
print("Storm: "+str(forecaster.will_have_storm()))
print("Clear-Sky: "+str(forecaster.will_have_clear()))
