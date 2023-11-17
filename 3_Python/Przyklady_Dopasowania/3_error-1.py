# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 3. Niepewności pomiarowe I.

import numpy as np
import matplotlib.pyplot as plt


###############################################################################
# Wczytanie danych doświadczalnych.
###############################################################################

data = np.loadtxt("data_2.txt")
x     = data[:, 0] # [wiersz, kolumna], tu: wszystkie wiersze i pierwsza (zerowa) kolumna.
y     = data[:, 1] # [wiersz, kolumna], tu: wszystkie wiersze i druga (pierwsza) kolumna.
err_x = data[:, 2] # [wiersz, kolumna], tu: wszystkie wiersze i trzecia (druga) kolumna.
err_y = data[:, 3] # [wiersz, kolumna], tu: wszystkie wiersze i czwarta (trzecia) kolumna.


###############################################################################
# Prezentacja danych doświadczalnych wraz z niepewnościami pomiarowymi.
###############################################################################

fig, ax = plt.subplots(2, 2)

ax[0][0].grid()
ax[0][0].plot(x, y, ".")

ax[0][1].grid()
ax[0][1].errorbar(x, y, yerr = err_y, fmt = ".")

ax[1][0].grid()
ax[1][0].errorbar(x, y, xerr = err_x, fmt = ".")

ax[1][1].grid()
ax[1][1].errorbar(x, y, xerr = err_x, yerr = err_y, fmt = ".")

plt.show()