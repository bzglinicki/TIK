# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 1. Wykreślanie funkcji - interfejs pyplot.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)


plt.xlim(0, 2*np.pi)
plt.ylim(-1.2, 1.2)

plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title(r"$y = \sin x$")

plt.plot(x, y)
plt.show()


plt.xlim(0, 2*np.pi)
plt.ylim(-1.2, 1.2)

plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("$y = \sin x$")

plt.plot(x, y)
plt.savefig("sin.png")