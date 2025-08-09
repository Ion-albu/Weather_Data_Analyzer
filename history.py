"""  Acest fișier conține funcția pentru salvarea istoricului vremii într-un fișier text.
     La fiecare apel, se adaugă o nouă înregistrare cu dată, ora, temperatură, descriere, umiditate și vânt.
"""
from datetime import datetime

def salveaza_istoric(weather_data):
    with open("istoric_vreme.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Vremea în {weather_data['oraș']}:\n")
        f.write(f"  - Temperatură: {weather_data['temperatură']}°C\n")
        f.write(f"  - Descriere: {weather_data['descriere']}\n")
        f.write(f"  - Umiditate: {weather_data['umiditate']}%\n")
        f.write(f"  - Viteza vântului: {weather_data['vânt']} m/s\n")
        f.write("\n")
