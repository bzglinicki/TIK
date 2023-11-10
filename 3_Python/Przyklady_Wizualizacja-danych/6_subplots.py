# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 6. Wiele wykresów na osobnych rysunkach.

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x**2)


fig1, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Pojedynczy wykres.")
plt.show()


fig2, axs = plt.subplots(2)
fig2.suptitle("Wykresy rozmieszczone wertykalnie")
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()


fig3, (ax1, ax2) = plt.subplots(1, 2)
fig3.suptitle("Wykresy rozmieszczone horyzontalnie")
ax1.plot(x, y)
ax2.plot(x, -y)
plt.show()