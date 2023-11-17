# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 6. Histogramy I.

import numpy as np
import matplotlib.pyplot as plt
import itertools


###############################################################################
# Przygotowanie spreparowanych danych doświadczalnych.
###############################################################################

# Rozkład Gaussa (normalny).

# Parametry rozkładu.
mu    = 1.3 # Wartość średnia.
sigma = 0.4 # Odchylenie standardowe.

# Losujemy 1000 punktów.
N = 3000

x = np.random.default_rng().normal(mu, sigma, N)


###############################################################################
# Rysowanie histogramu.
###############################################################################

plt.hist(x)
plt.show()