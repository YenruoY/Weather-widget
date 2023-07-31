import requests
import json
from datetime import datetime

latitude = "<Enter location latitude>" 
longitude = "<Enter location longitude>"

# Enter your Openweather API key
api_key = "<Enter API key>"
 

def main():
    d1 = datetime.today().strftime("%Y-%m-%d")
    t1 = datetime.now().strftime("%H:%M:%S")

    url = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&dt={2}&units=metric&appid={3}".format(latitude, longitude, d1, api_key)

    r = requests.get(url)
    data = r.json()
    data = data['current']

    temp = data['feels_like']
    humid = data['humidity']
    wind_speed = data['wind_speed']

    print(" :{0}℃   🌢:{1}  ⛱:{2}".format(temp, humid, wind_speed))


if __name__ == '__main__':
    main()
