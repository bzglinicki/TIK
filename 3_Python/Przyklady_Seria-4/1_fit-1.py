# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 1. Dopasowanie prostej do danych doświadczalnych.

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


###############################################################################
# Wczytanie danych doświadczalnych.
###############################################################################

data = np.loadtxt("data_1.txt")
x = data[:, 0] # [wiersz, kolumna], tu: wszystkie wiersze i pierwsza (zerowa) kolumna.
y = data[:, 1] # [wiersz, kolumna], tu: wszystkie wiersze i druga (pierwsza) kolumna.


###############################################################################
# Dopasowanie prostej y = a x + b do danych doświadczalnych.
###############################################################################

# Funkcja zadająca krzywą y = f(x), która ma zostać dopasowana.
# Na liście argumentów muszą się też znaleźć parametry dopasowania: a i b.
def f(x, a, b):
    return a*x + b

# Krotka zawierająca początkowe wartości parametrów dopasowania: a i b.
p0 = (0, 0)

# scipy.optimize.curve_fit dokonuje dopasowania.
# p będzie tablicą (ndarray) zawierającą dopasowane parametry.
# pcov będzie tablicą (ndarray) zawierającą macierz kowariancji.
p, pcov = scipy.optimize.curve_fit(f, x, y, p0)


###############################################################################
# Prezentacja danych doświadczalnych i wyników dopasowania.
###############################################################################

# Wypisujemy wyniki na standardowe wyjście.
print("Dopasowanie prostej y = a x + b")
print(f"   Parametry: {p}")
print(f"   Błędy: {np.sqrt(np.diag(pcov))}")

# Wykreślamy dane doświadczalne wraz z dopasowaniem.
fig, ax = plt.subplots()

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$");
ax.set_title("Prosta $y = ax + b$")

ax.plot(x, y, ".", label = "Dane doświadczalne")

# p jest tablicą, musimy napisać *p, aby przekazać jej wartości jako niezależne zmienne.
ax.plot(x, f(x, *p), label = "Dopasowanie")

ax.legend()
plt.show()