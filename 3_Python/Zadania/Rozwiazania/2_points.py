# Technologie informacyjne i komunikacyjne
# Python - zadania.
# Zadanie 2. points – Rysowanie wykresów ciągów.

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (1/3)*np.cos(2*x + 8) + 4


u = np.array([10*k for k in range(1, 11)])
v = np.array([5*k for k in range(1, 11)])

fig, ax = plt.subplots()

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Zadanie 2. Rysowanie wykresów ciągów.")

ax.scatter(u, f(u), marker = "^", color = "yellow", label = r"$\left( u_k , \, f \left( u_k \right) \right) $")
ax.scatter(v, f(v), marker = "+", color = "red", label = r"$\left( v_k , \, f \left( v_k \right) \right) $")
ax.plot(u - v/2, f(u + 2*v), "-g", marker = ".", markerfacecolor = "blue", markeredgecolor = "blue", markersize = "10", label = r"$\left( u_k - v_k / 2 , \, f \left( u_k + 2 v_k \right) \right) $")

ax.legend()

plt.show()
fig.savefig("points.pdf")