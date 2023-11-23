# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 7. Niepewności pomiaru.

import numpy as np
import matplotlib.pyplot as plt


# Przykładowe dane
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# Przykładowe wartości niepewności pomiaru
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)


# Rysujemy
fig4, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, sharex=True, figsize=(12, 6))

ax0.set_title("Wszystkie niepewności")
ax0.errorbar(x, y1, yerr = y1err)
ax0.errorbar(x, y2, yerr = y2err)

ax1.set_title("Wybrane niepewności - co szósta")
ax1.errorbar(x, y1, yerr = y1err, errorevery = 6)
ax1.errorbar(x, y2, yerr = y2err, errorevery = 6)

ax2.set_title("Druga seria przesunięta o 3")
ax2.errorbar(x, y1, yerr = y1err, errorevery = (0, 6))
ax2.errorbar(x, y2, yerr = y2err, errorevery = (3, 6))

fig4.suptitle("Niepewności pomiaru - przykłady")

plt.show()