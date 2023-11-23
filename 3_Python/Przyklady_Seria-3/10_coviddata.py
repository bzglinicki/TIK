# Technologie informacyjne i komunikacyjne
# Przykłady - wizualizacja danych.
# Przykład 10.


import urllib.request
import shutil
from datetime import datetime
import matplotlib.pyplot as plt


#***********************************************************************************
# Pobieranie pliku z danymi
#***********************************************************************************

url = "https://covid.ourworldindata.org/data/jhu/full_data.csv"

with urllib.request.urlopen(url) as response, open("coviddata.csv", "wb") as out_file:
    shutil.copyfileobj(response, out_file)


#***********************************************************************************
# Analiza danych - krok I:
# zbiór dostępnych krajów
#***********************************************************************************

# Tworzymy zbiór, na początku pusty, w którym będziemy przechowywać nazwy krajów.

locations = set()

# Analizujemy plik z danymi linia po linii, wydobywając z każdej linii informację
# o tym, jakiego kraju dotyczą zawarte w niej dane, a następnie umieszczamy nazwę
# tego kraju w zbiorze locations. Jeśli nazwa kraju, którą chcemy dodać do zbioru,
# już się w nim znajduje, nie zostanie wykonana żadna akcja - zbiór nie dopuszcza
# duplikatów.

with open("coviddata.csv") as datafile:
   # Pierwsza linia pliku w formacie CSV nie zawiera właściwych danych, lecz
   # nagłówki kolejnych kolumn, dlatego chcemy ją pominąć. Funkcja next przesuwa
   # kursor wskazujący aktualnie czytaną linię pliku na następną pozycję - dzięki
   # jej wywołaniu w tym miejscu następująca po niej pętla for rozpocznie
   # przeglądanie pliku nie od pierwszej, ale od drugiej jego linii.

   next(datafile)

   for line in datafile:
      data = line.split(",")
      locations.add(data[1])   # Element nr 1 listy data zawiera nazwę kraju.


#***********************************************************************************
# Interakcja z użytkownikiem:
# wypisanie nazw dostępnych krajów i prośba o wskazanie jednego z nich
#***********************************************************************************

print("Krzywa zachorowań na COVID-19")
print("=============================\n\n")
print("Dostępne lokalizacje:\n")

# Wypisujemy zawartość zbioru locations, nie czynimy tego jednak bezpośrednio.
# Funkcja sorted przekształca zbiór w listę, której elementy są posortowane
# (w przypadku łańcuchów znaków - alfabetycznie). Elementy zbioru nie są
# ponumerowane - gdybyśmy pominęli funkcję sorted, zostałyby one wypisane
# w przypadkowej kolejności.

for loc in sorted(locations): print(loc)
print()   # Pusta linia dla przejrzystości.

# Prosimy użytkownika o wskazanie interesującej go lokalizacji w nieskończonej
# pętli. Dzięki temu prośba będzie się pojawiała tak długo, aż użytkownik poda
# poprawną nazwę kraju (wówczas pętla zostanie przerwana za pomocą komendy
# break) lub zakończy działanie programu, wpisując "quit".

while True:
   location = input("Wybierz lokalizację lub wpisz quit, by zakończyć działanie programu: ")
   if location == "quit": quit()       # Zakończenie pracy programu.
   elif location in locations: break   # Nazwa kraju poprawna - zakończenie pętli.
   else: print(f"{location} nie jest żadną z dostępnych lokalizacji.\n")


#***********************************************************************************
# Analiza danych - krok II:
# informacje o zachorowaniach w wybranym kraju
#***********************************************************************************

# Tworzymy pusty słownik. Będziemy w nim zapisywać dane o zachorowaniach w wybranym
# kraju. Każdy wpis w tym słowniku będzie opisywał konkretny dzień: klucz będzie
# przechowywał datę, zaś wartość - dzienną liczbę zachorowań.

cases = {}

# Jak poprzednio, analizujemy plik z danymi linia po linii.

with open("coviddata.csv") as datafile:
   # Znaczenie tej instrukcji zostało wyjaśnione wyżej. W tym miejscu możliwe jest
   # jej pominięcie - pierwsza linia pliku z danymi zostanie i tak odrzucona przez
   # instrukcję warunkową if sprawdzającą zgodność nazwy kraju z tą, którą wybrał
   # użytkownik. Zostawiamy jednak to polecenie dla przejrzystości kodu.

   next(datafile)

   for line in datafile:
      data = line.split(",")

      # Sprawdzamy, czy aktualnie analizowana linia zawiera dane dotyczące kraju,
      # który wybrał użytkownik.

      if data[1] == location:
         # Jeśli w aktualnej linii dzienna liczba zachorowań nie została podana,
         # przypisujemy jej wartość 0. Pominięcie tego kroku skutkowałoby
         # zgłoszeniem przez funkcję float (w następnej linii) wyjątku
         # ValueError.

         if data[2] == "": data[2] = 0

         # Zapisujemy w słowniku cases datę i dzienną liczbę zachorowań.
         # Data przechowywana jest nie jako łańcuch znaków, lecz jako obiekt
         # dedykowanego typu datetime, zdefiniowanego w module datetime.
         # Dzięki temu etykiety na osi odciętych wykresu, który niebawem
         # narysujemy, będą wyświetlane z odpowiednim krokiem, takim, by opis
         # osi był czytelny. Funkcja strptime z modułu datetime konwertuje
         # łańcuch znaków na obiekt typu datetime.

         cases[datetime.strptime(data[0], "%Y-%m-%d")] = float(data[2])


#***********************************************************************************
# Wykreślenie krzywej zachorowań i wyświetlenie wykresu
#***********************************************************************************

plt.plot(list(cases.keys()), list(cases.values()))

plt.xlabel("Data")
plt.ylabel("Dzienna liczba zachorowań")
plt.title(f"Krzywa zachorowań na COVID-19 dla {location}")
plt.grid()
plt.show()