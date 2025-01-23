#1
n = int(input("Podaj liczbę n: "))
for i in range(1, n + 1):
    print("*" * i)
#2
n = int(input("Podaj liczbę n: "))
result = 1
for _ in range(n):
    a = float(input("Podaj liczbę: "))
    result *= (a + 1)
print("Wynik:", result)
#3 
def operacje_na_stringu(tekst):
    """Usuwa cyfry i spacje, a następnie wyświetla co czwarty znak od końca."""
    nowy_tekst = ""
    for znak in tekst:
        if not znak.isdigit() and znak != " ":
            nowy_tekst += znak

    # Wyświetlanie co czwartego znaku od końca
    print(nowy_tekst[::-4]) #krojenie odwróconego tekstu co 4 znak

# Przykład użycia
tekst = "W Roku Panskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalil dekret o 20%ej zniżce podatków!"
operacje_na_stringu(tekst)
#4
def szyfruj_tekst(tekst):
    """Szyfruje tekst przestawiając znaki parami."""
    zaszyfrowany_tekst = ""
    for i in range(0, len(tekst) - 1, 2):
        zaszyfrowany_tekst += tekst[i+1]
        zaszyfrowany_tekst += tekst[i]
    if len(tekst) % 2 != 0:
        zaszyfrowany_tekst += tekst[-1]
    return zaszyfrowany_tekst

# Przykład użycia:
tekst = input("Podaj tekst do zaszyfrowania: ")
zaszyfrowany = szyfruj_tekst(tekst)
print(f"Zaszyfrowany tekst: {zaszyfrowany}")
#5
def my_max(a, b, c):
    """Znajduje maksimum z trzech liczb."""
    maksimum = a
    if b > maksimum:
        maksimum = b
    if c > maksimum:
        maksimum = c
    return maksimum

# Przykład użycia
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))
maksimum = my_max(a, b, c)
print(f"Maksimum: {maksimum}")
#6
def iloczyn(*args):
    wynik = 1
    for liczba in args:
        wynik *= liczba
    return wynik

print("Iloczyn:", iloczyn(3, 5, 2, 7))
#7
def licz_cyfry(liczba):
    liczba = abs(liczba)  # Dla liczb ujemnych
    zerowe, niezerowe = 0, 0
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra == 0:
            zerowe += 1
        else:
            niezerowe += 1
        liczba //= 10
    return zerowe, niezerowe

liczba = int(input("Podaj liczbę: "))
zerowe, niezerowe = licz_cyfry(liczba)
print("Zerowe cyfry:", zerowe)
print("Niezerowe cyfry:", niezerowe)
