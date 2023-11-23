# Technologie informacyjne i komunikacyjne
# Przykłady - seria 1. Podstawy języka Python.
# Przykład 4. nextprime – Następna liczba pierwsza.


###############################################################################
# Funkcja is_prime
###############################################################################

def is_prime(n):
    """Zwraca True, gdy liczba n jest pierwsza, lub False w przeciwnym przypadku.

    Wykorzystano prosty algorytm opisany na Wikipedii:
       https://en.wikipedia.org/wiki/Primality_test#Simple_methods
    """
    
    if n <= 1: return False   # Te dwie instrukcje można zapisać łącznie:
    if n <= 3: return True    #   if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


###############################################################################
# Funkcja next_prime
###############################################################################

def next_prime(n):
    """Zwraca najmniejszą liczbę pierwszą większą od n."""
    
    if (n <= 1): return 2

    k = n
    prime = False

    while not prime:
        k += 1
        prime = is_prime(k)

    return k
  

###############################################################################
# Główny program
###############################################################################

n = int(input("Podaj liczbę naturalną: "))
print(f"Najmniejsza liczba pierwsza większa od {n} to {next_prime(n)}.")