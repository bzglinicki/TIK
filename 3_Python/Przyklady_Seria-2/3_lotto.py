# Technologie informacyjne i komunikacyjne
# Przykłady - seria 2. Kolekcje.
# Przykład 3. lotto – Losowanie liczb.


# Generowanie liczb pseudolosowych.
import random


s = set()

while len(s) < 6:
    s.add(random.randint(1, 49))

print(*sorted(s))