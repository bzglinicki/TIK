# Technologie informacyjne i komunikacyjne
# Przykłady - seria 1. Podstawy języka Python.
# Przykład 6. Ciąg Fibonacciego. Program fibsum.

sum = 0 # Szukana suma wyrazów ciągu Fibonacciego.
a = 1   # Aktualny wyraz ciągu.
b = 2   # Następny wyraz ciągu.

while a <= 3000000:
    if a % 2 == 0: sum += a
    a, b = b, a + b

print(sum)