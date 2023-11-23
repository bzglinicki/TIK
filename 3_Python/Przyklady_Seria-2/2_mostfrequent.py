# Technologie informacyjne i komunikacyjne
# Przykłady - seria 2. Kolekcje.
# Przykład 2. mostfrequent – Najczęściej występujący element listy.


###############################################################################
# Funkcja most_frequent
###############################################################################

def most_frequent(lst):
    """Zwraca najczęściej występujący element listy."""

    k = lst[0]   # Dotychczas najczęściej występujący element.
    freq = 0     # Częstotliwość występowania elementu k.

    for i in lst:
        curr_freq = lst.count(i)   # Częstotliwość występowania elementu i.
        if(curr_freq > freq):
            freq = curr_freq
            k = i

    return k


###############################################################################
# Główny program
###############################################################################

input_str = input("Podaj listę elementów oddzielonych przecinkiem:\n   ")
input_lst = input_str.split(",")

print(f"Najczęściej występujący element listy: {most_frequent(input_lst)}.")