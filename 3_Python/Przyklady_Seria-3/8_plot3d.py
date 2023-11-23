# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 8. Wykreślanie funkcji dwóch zmiennych.

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Przygotowanie danych
x = y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = x**2 * y**2


# Rysujemy
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection = "3d")

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_title("Wykres funkcji $f(x, \, y) = x^2 y^2$")

ax.plot_surface(x, y, z)

plt.show()