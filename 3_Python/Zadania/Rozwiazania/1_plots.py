# Technologie informacyjne i komunikacyjne
# Python - zadania.
# Zadanie 1. plots – Rysowanie wykresów funkcji.

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return - 3*x**4 + 7*x**3 - 4*x + 6

def g(x):
    return - 2*x**2 - 8*x + 1 + np.sin(x)

def u(x):
    return np.exp(- x + 5)

def v(x):
    return np.sqrt(x + 3)


x = np.linspace(-8, 8, 200)


fig, ax = plt.subplots()

ax.set_xlim(-8, 8)
ax.set_ylim(-5, 10)

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Zadanie 1. Rysowanie wykresów funkcji.")

ax.plot(x, f(x), "-y", label = r"$y = - 3x^4 + 7x^3 - 4x + 6$")
ax.plot(x, g(x), "--r", label = r"$y = - 2x^2 - 8x + 1 + \sin x$")
ax.plot(x, u(x), ":b", label = r"$y = \mathrm{e}^{- x + 5}$")
ax.plot(x, v(x), "-.g", label = r"$y = \sqrt{x + 3}$")

ax.legend()

plt.show()
fig.savefig("plots.pdf")