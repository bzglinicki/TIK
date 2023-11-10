# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 2. Wykreślanie funkcji - interfejs obiektowy.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.cos(x)

fig1, ax = plt.subplots()

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.2, 1.2)

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$");
ax.set_title(r"$y = \cos x$")

ax.plot(x, y)

plt.show()
fig1.savefig("cos.pdf")