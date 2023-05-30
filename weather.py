#the function which displays the weather
#the structure of this code was obtained from geeksforgeeks.org
#api key is the property of Yash Suresh, no unauthorised use allowed

import requests
from datetime import datetime

def ReturnWeather():
    api_key = "b6d4314e38e39ed7a048ad016e65a0dc"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Nottingham"
    url = url + "appid=" + api_key + "&q=" + city
    response = requests.get(url)

    results = response.json()
    numbers = results["main"]
    weather = results["weather"]
    weather_description = weather[0]["description"]

    current_temp = numbers["temp"]
    current_temp = int(current_temp-273)
    degree_sign = u'\N{DEGREE SIGN}'
    return (str(current_temp) + degree_sign + "C, " + weather_description)


