"""  Acest fișier desenează un grafic cu evoluția temperaturilor pe zile.
     X = ziua înregistrării, Y = temperatura.
"""
import matplotlib.pyplot as plt

def afiseaza_grafic_temperaturi(zile, temperaturi):
    plt.plot(zile, temperaturi, marker='o')
    plt.title("Evoluția temperaturii")
    plt.xlabel("Ziua")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    plt.show()
