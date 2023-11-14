# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 2. Różne dopasowania do tych samych danych doświadczalnych.

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

from numpy import array, exp
from scipy.optimize import curve_fit


###############################################################################
# Preparowanie danych doświadczalnych.
###############################################################################

y = array([12, 11, 13, 15, 16, 16, 15, 14, 15, 12, 11, 12, 8, 10, 9, 7, 6])
x = array(range(len(y)))


###############################################################################
# Dopasowanie różnych krzywych do danych doświadczalnych.
###############################################################################

# Funkcje, które mają zostać dopasowane; na liście argumentów muszą się też znaleźć parametry dopasowania.
def f1(x, a, b, c):
    return a*x**2 + b*x + c

def f2(x, a, b, c):
    return a*x**3 + b*x + c

def f3(x, a, b, c):
    return a*x**3 + b*x**2 + c

def f4(x, a, b, c):
    return a*exp(b*x) + c

# Dopasowanie krzywej y = f1(x).
params, _ = curve_fit(f1, x, y)
a, b, c = params[0], params[1], params[2]
yfit1 = a*x**2+b*x+c

# Dopasowanie krzywej y = f2(x).
params, _  = curve_fit(f2, x, y)
a, b, c = params[0], params[1], params[2]
yfit2 = a*x**3+b*x+c

# Dopasowanie krzywej y = f3(x).
params, _  = curve_fit(f3, x, y)
a, b, c = params[0], params[1], params[2]
yfit3 = a*x**3+b*x**2+c

# Dopasowanie krzywej y = f4(x).
params, _  = curve_fit(f4, x, y)
a, b, c = params[0], params[1], params[2]
yfit4 = a*exp(x*b)+c


###############################################################################
# Prezentacja wyników dopasowania.
###############################################################################

plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(x, y, "bo", label = "Dane doświadczalne (spreparowane).")
plt.plot(x, yfit1, label = "Dopasowana krzywa $y=ax^2 + bx + c$")
plt.plot(x, yfit2, label = "Dopasowana krzywa $y=ax^3 + bx + c$")
plt.plot(x, yfit3, label = "Dopasowana krzywa $y=ax^3 + bx^2 + c$")
plt.plot(x, yfit4, label = "Dopasowana krzywa $y=a \, \exp (bx) + c$")

plt.legend(shadow = True)
plt.show()