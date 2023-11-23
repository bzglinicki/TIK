# Technologie informacyjne i komunikacyjne
# Przykłady - seria 2. Kolekcje.
# Przykład 7. Ciąg Collatza. Program collatz.


###############################################################################
# Funkcja collatz
###############################################################################

def collatz(n):
    """Zwraca początkowe wyrazy ciągu Collatza aż do pierwszego wyrazu o wartości 1 włącznie."""
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield n
        else:
            n = 3 * n + 1
            yield n

""" KOMENTARZ
Omówienie i przykłady użycia słowa kluczowego yield:
   https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
   https://realpython.com/introduction-to-python-generators/
"""


###############################################################################
# Główny program
###############################################################################

k = int(input("Podaj liczbę naturalną: "))
print(f"Ciąg Collatza zaczynający się od {k} do pierwszego wystąpienia 1:")
print(f"   {list(collatz(k))}")