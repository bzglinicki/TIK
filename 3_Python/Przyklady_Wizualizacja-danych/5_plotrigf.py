# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 5. Wykreślanie funkcji - formatowanie wykresów.

import numpy as np
import matplotlib.pyplot as plt


# Pomocnicza funkcja plot - przygotowuje dane i rysuje wykresy
def plot():
   # Przygotowanie danych

   x = x = np.linspace(-0.9, 0.9, 200)
   y_sin = np.sin(x)
   y_tg = np.tan(x)


   # Rysowanie wykresów

   plt.plot(x, x, ":y", label = "$y = x$")
   plt.plot(x, y_sin, "--r", label = r"$y = \sin x$")
   plt.plot(x, y_tg, "-.b", label = r"$y = \mathrm{tg} x$")

   plt.grid()
   plt.xlabel("$x$")
   plt.ylabel("$y$")
   plt.title("Wykresy funkcji: liniowej, sinus i tangens.")
   plt.legend()


# Wyświetlenie rysunku na ekranie

plot()
plt.show()


# Zapis rysunku do pliku

print("Czy zapisać rysunek do pliku? Jeśli tak, podaj format (png, jpg, svg lub pdf).")
format = input()

if format.lower() == "png":
   plot()
   plt.savefig("trigplot.png", dpi = 300, transparent = True)
   print("Rysunek został zapisany w pliku trigplot.png.")
elif format.lower() == "jpg":
   plot()
   plt.savefig("trigplot.jpg", dpi = 300)
   print("Rysunek został zapisany w pliku trigplot.jpg.")
elif format.lower() == "svg":
   plot()
   plt.savefig("trigplot.svg")
   print("Rysunek został zapisany w pliku trigplot.svg.")
elif format.lower() == "pdf":
   plot()
   plt.savefig("trigplot.pdf")
   print("Rysunek został zapisany w pliku trigplot.pdf.")
else:
   print("Rysunek nie został zapisany.")