# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 6. Wiele wykresów na osobnych rysunkach.

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x**2)


fig, axs = plt.subplots(2, 1)
fig.suptitle("Wykresy rozmieszczone wertykalnie")
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()

fig, axs = plt.subplots(2, 1, sharex = True)
fig.suptitle("Wykresy rozmieszczone wertykalnie - wspólna oś x.")
axs[0].plot(x, y)
axs[1].plot(x + 1, -y)
plt.show()

fig, axs = plt.subplots(3, 1, sharex = True, sharey = True)
fig.suptitle("Wykresy rozmieszczone wertykalnie - wspólna obie osie.")
axs[0].plot(x, y ** 2)
axs[1].plot(x, 0.3 * y, 'o')
axs[2].plot(x, y, '+')
plt.show()


fig, axs = plt.subplots(1, 2)
fig.suptitle("Wykresy rozmieszczone horyzontalnie")
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()