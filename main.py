"""
Script basico para obtener info del tiempo desde OpenWeather.com
* Temperatura
* Viento
* Lluvia
...
User: gzubiete@gmail.com
Password: galder12
"""

import requests
import json
import utils
from datetime import datetime

api_key = "f8f08833aa0da7a49af44561efc983ee"
lat = "43.2348"
lon = "-2.8827"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&appid=" + api_key + "&units=metric&lang=ES"
air_pol = "http://api.openweathermap.org/data/2.5/air_pollution?lat=" + lat + "&lon=" + lon + "&appid=" + api_key

response = requests.get(url)
data = json.loads(response.text)
desc = data["current"]["weather"][0]["description"]
print(str(datetime.fromtimestamp(data["current"]["dt"])))
print(desc.capitalize()) 
print("Temperatura:\t" + str(data["current"]["temp"]) + " ºC")
print("Sensación:\t" + str(data["current"]["feels_like"]) + " ºC")
print("Presion:\t" + str(data["current"]["pressure"])+ " hPa")
print("Humedad:\t" + str(data["current"]["humidity"])+ " %")
print("Punto de rocío:\t" + str(data["current"]["dew_point"])+ " ºC")
viento = data["current"]["wind_speed"] * 3.6
print("Viento:\t\t" + str(viento)+ " km/h")
print("Direccion:\t" + str(utils.degrees_to_direction(data["current"]["wind_deg"])))
print()

response_aq = requests.get(air_pol)
data_aq = json.loads(response_aq.text)
aq = data_aq["list"][0]["components"]
calidad = data_aq["list"][0]["main"] ["aqi"]
if calidad == 1:
    print("Calidad aire:\tMUY BUENA")
elif calidad == 2:
    print("Calidad aire:\tBUENA")
elif calidad == 3:
    print("Calidad aire:\tNORMAL")
elif calidad == 4:
    print("Calidad aire:\tMEDIOCRE")
elif calidad == 5:
    print("Calidad aire:\tMALA")
else:
    print("Calidad aire:\tNO DATA")
    
print("Monóxido de Carbono (CO):\t" + str(aq["co"]) + " ug/m3")
print("Monóxido de Nitrógeno (NO):\t" + str(aq["no"]) + " ug/m3")
print("Dióxido de Nitrógeno (NO2):\t" + str(aq["no2"]) + " ug/m3")
print("Ozono (O3):\t\t\t" + str(aq["o3"]) + " ug/m3")
print("Dióxido de Azufre (SO2):\t" + str(aq["so2"]) + " ug/m3")
print("Amoniaco (NH3):\t\t\t" + str(aq["nh3"]) + " ug/m3")
print("PM2.5:\t\t\t\t" + str(aq["pm2_5"]) + " ug/m3")
print("PM10:\t\t\t\t" + str(aq["pm10"]) + " ug/m3")

