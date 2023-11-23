# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 3. Wykreślanie funkcji przekazanej jako argument.

import numpy as np
import matplotlib.pyplot as plt


#***********************************************************************************
# Funkcja plotf
#***********************************************************************************

def plotf(f, a, b, N):
   x = np.linspace(a, b, N)
   y = f(x)
   
   plt.plot(x, y)

   plt.grid()
   plt.xlabel("$x$")
   plt.ylabel("$y$")
   plt.title("$y = f(x)$")
   
   plt.show()


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Pomocnicza funkcja f - zwraca wartości wykreślanej funkcji
def f(x):
   return x * np.sin(x) - x**2

print("Wykres funkcji f(x) = x sin x - x^2 w przedziale [a, b], N punktów.")
a = float(input("   a = "))
b = float(input("   b = "))
N = int(input("   N = "))

plotf(f, a, b, N)