# Technologie informacyjne i komunikacyjne
# Przykłady - seria 1. Podstawy języka Python.
# Przykład 3. qeq – Rozwiązywanie równań kwadratowych.


# math - funkcje matematyczne.
import math

# cmath - funkcje matematyczne liczb zespolonych.
import cmath


print("ax^2 + bx + c = 0")
a = float(input("   a = "))
b = float(input("   b = "))
c = float(input("   c = "))
print()   # Pusta linia dla estetyki.

delta = (b**2) - (4*a*c)

if delta == 0:
    x0 = -b / (2*a)
    print(f"Rozwiązanie:\n   x0 = {x0:.2f}")
elif delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Rozwiązania:\n   x1 = {x1:.2f}\n   x2 = {x2:.2f}")
else:
    x1 = (-b - cmath.sqrt(delta)) / (2*a)
    x2 = (-b + cmath.sqrt(delta)) / (2*a)
    print(f"Rozwiązania:\n   x1 = {x1:.2f}\n   x2 = {x2:.2f}")