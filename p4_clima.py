import requests
import os
from dotenv import  load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
ciudad = input("De que ciudad quieres saber el clima: ")

url = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid="+api_key+"&units=metric&lang=es"
respuesta = requests.get(url)
datos = respuesta.json()
try:

    print("Ciudad:", datos["name"])
    print("Temperatura:", datos["main"]["temp"])
    print("Descripcion:", datos["weather"][0]["description"])
except:
    print("Ciudad no encontrada")