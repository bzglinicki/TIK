# Technologie informacyjne i komunikacyjne
# Przykłady - seria 2. Kolekcje.
# Przykład 1. times – Tabliczka mnożenia.


# Argumenty wywołania programu.
import sys


###############################################################################
# Funkcja times
###############################################################################

def times(n):
    """Zwraca listę [n, 2n, ..., 10n]"""
    return [k * n for k in range(1, 11)]


###############################################################################
# Główny program
###############################################################################

m = int(sys.argv[1])

res = times(m)

for i in range(1, 11):
    # Dodatkowa spacja przed liczbami mniejszymi od 10 dla czytelności.
    if i < 10:
        print(" ", end = "")
    
    print(f"{i} x {m} = {res[i - 1]}")