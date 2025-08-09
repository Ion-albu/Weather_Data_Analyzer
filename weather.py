""" Acest fișier conține funcția care preia datele meteo din API-ul OpenWeatherMap.
    Funcția returnează un dicționar cu informații despre vreme sau None dacă e eroare.
"""
import requests

def get_weather(city_name, api_key):
    # URL pentru cererea către API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ro"
    response = requests.get(url)

    if response.status_code == 200:
        # Convertim răspunsul în format Json
        data = response.json()
        # Extragem informațiile importante
        weather = {
            "oraș": data["name"],
            "temperatură": data["main"]["temp"],
            "descriere": data["weather"][0]["description"],
            "umiditate": data["main"]["humidity"],
            "vânt": data["wind"]["speed"]
        }
        return weather
    else:
        # Dacă orașul nu este găsit sau apare altă eroare
        return None
