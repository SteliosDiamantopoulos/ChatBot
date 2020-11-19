import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();
def speak_weather(result,city):
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("Wind speed: {} m/s".format(result['wind']['speed']))
	speak("Description: {}".format(result['weather'][0]['description']))
	speak("Weather: {}".format(result['weather'][0]['main']))
def main():
	speak("Which city are u interested in?")
    city=input(takeCommand().lower())
	print(city)
	try:
	  city_place='q='+city;
	  w_data=weather_data(city_place);
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
if __name__=='__main__':
	main()
