# Technologie informacyjne i komunikacyjne
# Przykłady - seria 2. Kolekcje.
# Przykład 4. intersection – Część wspólna zbiorów liczb całkowitych.


###############################################################################
# Funkcja intersection
###############################################################################

def intersection(lsta, lstb):
    """Zwraca zbiór stanowiący część wspólną list lsta i lstb."""

    return set([value for value in lsta if value in lstb])


###############################################################################
# Główny program
###############################################################################

input_a_str = input("Podaj pierwszy ciąg liczb całkowitych:\n   ")
input_a_lst = [int(k) for k in input_a_str.split(" ")]

input_b_str = input("Podaj drugi ciąg liczb całkowitych:\n   ")
input_b_lst = [int(k) for k in input_b_str.split(" ")]

print(*sorted(intersection(input_a_lst, input_b_lst)))