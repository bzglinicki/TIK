# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 5. Dopasowanie krzywej do danych doświadczalnych z niepewnościami pomiaru.

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


###############################################################################
# Wczytanie danych doświadczalnych.
###############################################################################

data = np.loadtxt("data_3.txt")
x     = data[:, 0] # [wiersz, kolumna], tu: wszystkie wiersze i pierwsza (zerowa) kolumna.
y     = data[:, 1] # [wiersz, kolumna], tu: wszystkie wiersze i druga (pierwsza) kolumna.
err_y = data[:, 2] # [wiersz, kolumna], tu: wszystkie wiersze i trzecia (druga) kolumna.


###############################################################################
# Dopasowanie krzywej do danych doświadczalnych.
###############################################################################

# Funkcja zadająca krzywą y = f(x), która ma zostać dopasowana.
# Na liście argumentów muszą się też znaleźć parametry dopasowania.
def f(x, a, b, c, d, e, f, g):
    return a*np.exp(b*(x - c)**2) + d*np.exp(e*(x - f)**2) + g

# Krotka zawierająca początkowe wartości parametrów dopasowania.
p0 = (30, -1, 1, 0, 0, 0, 0)

# scipy.optimize.curve_fit dokonuje dopasowania.
# p będzie tablicą (ndarray) zawierającą dopasowane parametry.
# pcov będzie tablicą (ndarray) zawierającą macierz kowariancji.
p, pcov = scipy.optimize.curve_fit(f, x, y, p0, sigma = err_y)


###############################################################################
# Prezentacja danych doświadczalnych i wyników dopasowania.
###############################################################################

# Wypisujemy wyniki na standardowe wyjście.
print("Dopasowanie sumy dwóch krzywych Gaussa")
print(f"   Parametry: {p}")
print(f"   Błędy: {np.sqrt(np.diag(pcov))}")

# Wykreślamy dane doświadczalne wraz z dopasowaniem.
fig, ax = plt.subplots()

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$");
ax.set_title("Suma dwóch krzywych Gaussa")

ax.errorbar(x, y, yerr = err_y, fmt = ".", label = "Dane doświadczalne")

# p jest tablicą, musimy napisać *p, aby przekazać jej wartości jako niezależne zmienne.
ax.plot(x, f(x, *p), label = "Dopasowanie")

ax.legend()
plt.show()