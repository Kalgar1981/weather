import requests
import json
import utils
from datetime import datetime


def get_api_data():

    fich = open("config", "r")
    content = fich.readlines()
    fich.close()
    linea = content[2].split(": ")
    return linea[1]


def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + utils.LAT + "&lon=" + utils.LONG + "&appid=" + get_api_data() + "&units=metric&lang=ES"

    response = requests.get(url)
    data = json.loads(response.text)
    if response.status_code != 200:
        return str(data["cod"])

    # Descripcion del tiempo (despejado, nublado, etc...)
    desc = data["current"]["weather"][0]["description"].capitalize()
    # Hora de lectura de datos
    lectura = datetime.fromtimestamp(data["current"]["dt"])
    # Temperatura (ºC)
    temp = data["current"]["temp"]
    # Sensacion termica (ºC)
    sensacion = data["current"]["feels_like"]
    # Presion (hPa)
    presion = data["current"]["pressure"]
    # Humedad (%)
    humedad = data["current"]["humidity"]
    # Punto de rocío (ºC)
    punto_rocio = data["current"]["dew_point"]
    # Viento (m/s convertido a km/h)
    viento = data["current"]["wind_speed"] * 3.6
    # Direccion del viento (º convertido a texto)
    direccion = utils.degrees_to_direction(data["current"]["wind_deg"])

    return {"desc": desc, "time": lectura, "temp": temp, "sens": sensacion, "pres": presion, "hum": humedad,
            "dewp": punto_rocio, "wspd": viento, "wdir": direccion}


def get_polution_data():
    air_pol = "http://api.openweathermap.org/data/2.5/air_pollution?lat=" + utils.LAT + "&lon=" + utils.LONG + "&appid=" + get_api_data()

    response_aq = requests.get(air_pol)
    data_aq = json.loads(response_aq.text)
    aq = data_aq["list"][0]["components"]
    calidad = data_aq["list"][0]["main"]["aqi"]

    """
    Todas los valoes de medicion del aire tienen las mismas unidades: ug/m3 (microgramos por metro cubico)
    """
    # Monoxido de carbono
    co = aq["co"]
    # Monoxido de nitrogeno
    no = aq["no"]
    # Dioxido de nitrogeno
    no2 = aq["no2"]
    # Ozono
    o3 = aq["o3"]
    # Dioxidod e azufre
    so2 = aq["so2"]
    # Amoniaco
    nh3 = aq["nh3"]
    # PM2.5
    pm25 = aq["pm2_5"]
    # PM10
    pm10 = aq["pm10"]

    return {"calidad": calidad, "co": co, "no": no, "no2": no2, "o3": o3, "so2": so2, "nh3": nh3, "pm25": pm25, "pm10": pm10}