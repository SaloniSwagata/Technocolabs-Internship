import pyowm

degree_sign= u'\N{DEGREE SIGN}'

owm = pyowm.OWM('d90703eea69f90f613b88279fea113db')

# Three Hours Forecast
mgr = owm.weather_manager()
place = input("Enter the name of the city: ")
forecaster = mgr.forecast_at_place(place, '3h')
forecast = forecaster.forecast
weather_list = forecast.weathers

print('Three hours forecast (Times are in GMT):')
for weather in weather_list:
    temp = weather.temperature(unit='celsius')['temp']
    print(weather.reference_time('iso'), f'Temperature: {temp}{degree_sign}C')
