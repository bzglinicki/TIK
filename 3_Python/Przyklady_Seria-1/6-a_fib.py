# Technologie informacyjne i komunikacyjne
# Przykłady - seria 1. Podstawy języka Python.
# Przykład 6. Ciąg Fibonacciego. Program fib.


###############################################################################
# Funkcja fib
###############################################################################

def fib(n):
    """Zwraca n-ty wyraz ciągu Fibonacciego.
    
    Wykorzystano algorytm nr 3 ze strony
       https://www.ics.uci.edu/~eppstein/161/960109.html
    """
    
    if n < 1: return 0
    if n == 1 or n == 2: return 1
    
    a = 1
    b = 1

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b

""" KOMENTARZ
Analiza różnych algorytmów obliczania wyrazów ciągu Fibonacciego
dostępna jest na stronie
   https://www.ics.uci.edu/~eppstein/161/960109.html

Najprostsza, rekurencyjna implementacja funkcji fib() ma postać:

   def fib(n):
       if n < 1: return 0
       elif n == 1 or n == 2: return 1
       else: return fib(n-1) + fib(n-2)

Taka implementacja jest jednak wysoce nieoptymalna. Łatwo zauważyć,
że te same obliczenia będą wykonywane wielokrotnie.
"""


###############################################################################
# Główny program
###############################################################################

n = int(input("Podaj liczbę naturalną: "))
print(f"F_{n} = {fib(n)}")