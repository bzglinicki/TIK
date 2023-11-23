# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 4. Niepewności pomiarowe II.

import numpy as np
import matplotlib.pyplot as plt


###############################################################################
# Przygotowanie spreparowanych danych doświadczalnych.
###############################################################################

# Spreparowane wyniki pomiarów dwóch wielkości, y1 i y2, jako funkcji x.
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# Spreparowane niepewności pomiaru wielkości y1 i y2.
err_y1 = 0.1 + 0.1 * np.sqrt(x)
err_y2 = 0.1 + 0.1 * np.sqrt(x/2)


###############################################################################
# Prezentacja danych doświadczalnych wraz z niepewnościami pomiarowymi.
###############################################################################

fig, ax = plt.subplots(1, 3, sharex = True, figsize = (12, 6))

ax[0].set_title("Wszystkie niepewności")
ax[0].grid()
ax[0].errorbar(x, y1, yerr = err_y1, fmt = ".")
ax[0].errorbar(x, y2, yerr = err_y2, fmt = ".")

ax[1].set_title("Wybrane niepewności - co szósta")
ax[1].grid()
ax[1].errorbar(x, y1, yerr = err_y1, errorevery = 6, fmt = ".")
ax[1].errorbar(x, y2, yerr = err_y2, errorevery = 6, fmt = ".")

ax[2].set_title("Wybrane niepewności - przesunięte")
ax[2].grid()
ax[2].errorbar(x, y1, yerr = err_y1, errorevery = (0, 6), fmt = ".")
ax[2].errorbar(x, y2, yerr = err_y2, errorevery = (3, 6), fmt = ".")

fig.suptitle("Niepewności pomiaru - przykłady")

plt.show()