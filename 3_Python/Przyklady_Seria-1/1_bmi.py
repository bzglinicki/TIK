# Technologie informacyjne i komunikacyjne
# Przykłady - seria 1. Podstawy języka Python.
# Przykład 1. bmi – Wskaźnik masy ciała.

m = float(input("Podaj masę ciała (w kilogramach): "))
h = float(input("Podaj wzrost (w metrach): "))
print()   # Pusta linia dla estetyki.

bmi = m / (h**2)

print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
    print("Niedowaga.")
elif bmi >= 18.5 and bmi < 25:     # Wystarczyłoby sprawdzić, czy bmi < 25,
    print("Waga prawidłowa.")      # ponieważ możliwość bmi < 18.5 została już
elif bmi >= 25 and bmi < 30:       # zbadana wcześniej; dla elegancji kodu oraz
    print("Nadwaga.")              # przykładu użycia operatora and zostawiamy
else:                              # taką postać. Podobnie w kolejnym warunku.
    print("Otyłość.")