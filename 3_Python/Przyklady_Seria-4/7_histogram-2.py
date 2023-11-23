# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 7. Histogramy II.

import numpy as np
import matplotlib.pyplot as plt
import itertools


###############################################################################
# Wczytanie danych doświadczalnych.
###############################################################################

# Pierwszy wiersz pliku data_4.txt nie zawiera właściwych danych, a tylko
# nagłówki kolumn, dlatego pomijamy go, używając argumentu skiprows.
data = np.loadtxt("data_4.txt", skiprows = 1)


###############################################################################
# Rysowanie histogramu.
###############################################################################

fig, ax = plt.subplots(3, 2)

fig.suptitle("Wyniki kolokwium")

# Domyślnie elementy ax są tu indeksowane w postaci
#    ax[i, j],
# gdzie
#    i zmienia się od 0 do 2,
#    j zmienia się od 0 do 1,
# czyli wykresy są w ax "ułożone" w macierz 3 x 3. 
# Dla wygody chcemy zmienić sposób indeksowania na
#    ax[k],
# gdzie k zmienia się od 0 do 5, czyli chcemy, aby
# wykresy były w ax ułożone w macierz 6 x 1. Takie
# indeksowanie jedną zmienną ułatwi nam zapisanie
# pętli po wykresach, w której wartość zmiennej
# k będzie odpowiadała numerowi zadania. 
ax = list(itertools.chain.from_iterable(ax))

for i in range(0, 5):
    ax[i].hist(data[:,i], bins = [0, 0.5, 1, 1.5, 2])
    ax[i].set_title(f"Zad. {i+1}")

ax[5].hist(data.sum(axis = 1), bins = [0, 2.5, 5, 7.5, 10])
ax[5].set_title("Suma")

# Dostosowujemy odstępy pomiędzy wykresami na płótnie,
# by tytuły i opisy osi sąsiednich wykresów nie
# nachodziły na siebie.
fig.tight_layout()

plt.show()