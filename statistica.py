""" Acest fișier calculează statistici dintr-o listă de temperaturi.
    Returnează media, maximul și minimul.
"""
import numpy as np
def calculeaza_statistici(temperaturi):
    arr = np.array(temperaturi)
    return {
        "media": np.mean(arr),
        "max": np.max(arr),
        "min": np.min(arr)
    }