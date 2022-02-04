import numpy as np
import random

print()
losowa_liczba = np.random.random(1)
print("7.A generuje liczbe losowa z przedzialu (0,1)")
print(losowa_liczba)
print()
print("7.B Symulujemy karty")
pierwsza_karta, druga_karta, trzecia_karta = random.sample(range(1, 52), 3)
print(pierwsza_karta, druga_karta, trzecia_karta)
print()

if pierwsza_karta < 14 or druga_karta < 14 or trzecia_karta < 14:
    print("Wśród wyciągniętych kart jest przynajmniej jeden trefl")
    print()
else:
    print("Wśród wyciągniętych kart nie ma żadnego trefla")
    print()

print("7.C wykonujemy proby")

def losowanie(N):
    licznik_trefli = 0
    for i in range(N):
        pierwsza_karta, druga_karta, trzecia_karta = random.sample(range(1, 53), 3)
        if pierwsza_karta < 14 or druga_karta < 14 or trzecia_karta < 14:
            licznik_trefli += 1
    return licznik_trefli/N

n = 1
while True:
    if round(losowanie(n), 3) == 0.587:
        print(f"Oczekiwany wynik osiągnięto przy {n} prób")
        print()
        break
    n += 1