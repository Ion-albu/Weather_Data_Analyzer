"""# Acesta este fișierul principal al aplicației.
 - Primește orașul de la utilizator
 - Apelează funcția get_weather() pentru a lua datele din API
 - Afișează datele meteo pe ecran
 - Salvează datele în fișier text
 - Stochează temperaturile într-o listă pentru a calcula statistici
 - La final, afișează media/max/min și un grafic"""
from weather import get_weather
from history import salveaza_istoric
from statistica import calculeaza_statistici
from plot import afiseaza_grafic_temperaturi

API_KEY = "98abfe7c17535cabc7021221c35a4f83"  # Aceasta este cheia mea din OpenWeatherMap

def main():
    temperaturi = []  # lista pentru temperaturile înregistrate
    zile = []         # listă pentru numărul zilei (pentru grafic)

    zi = 1
    while True:
         # Se cere orașul
        city = input("\nIntrodu numele orașului (sau 'exit' pentru a ieși): ")

        if city.lower() == "exit":
            # Dacă utilizatorul scrie 'exit', se închide aplicația
            print("La revedere!")
            break

         # Luăm datele meteo din API
        result = get_weather(city, API_KEY)

        if result:
            # Dacă orașul a fost găsit, afișăm datele meteo
            print(f"\nVremea în {result['oraș']}:")
            print(f"Temperatură: {result['temperatură']}°C")
            print(f"Descriere: {result['descriere']}")
            print(f"Umiditate: {result['umiditate']}%")
            print(f"Viteza vântului: {result['vânt']} m/s")

           # Salvăm datele în fișier text
            salveaza_istoric(result)

            # Adăugăm temperatura în listă
            temperaturi.append(result['temperatură'])
            zile.append(zi)
            zi += 1
        else:
            print("❌ Nu am putut găsi orașul sau a apărut o eroare.")
   # După ce ieșim din buclă, dacă avem temperaturi salvate, calculăm statistici și afișăm graficul
    if temperaturi:
        stats = calculeaza_statistici(temperaturi)
        print(f"\nStatistici temperaturi înregistrate: Media={stats['media']:.2f}°C, Max={stats['max']}°C, Min={stats['min']}°C")
        afiseaza_grafic_temperaturi(zile, temperaturi)

if __name__ == "__main__":
    main()
