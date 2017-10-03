import pyowm
def weather():
	owm = pyowm.OWM('<enter API key>') #https://pyowm.readthedocs.io/en/latest/
									   #http://openweathermap.org/appid
	
	place = raw_input("Enter the place: ")
	observation = owm.weather_at_place(place)
	w = observation.get_weather()
	complete_temp = w.get_temperature('celsius') 
	for i in complete_temp:
		if(i=="temp"):
			print "The temperature is " + str(complete_temp[i]) + " Degrees celsius "


weather()