#1
n = int(input("Podaj liczbę n: "))
suma = 0
for _ in range(n):
    a = float(input("Podaj liczbę: "))
    suma += a**3
print("Wynik:", suma)
#2
suma_kwadratow = 0
while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba < 0:
        break
    suma_kwadratow += liczba**2
print("Suma kwadratów:", suma_kwadratow)
#3
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print("Iloczyn:", a * b)
#4
def operacje_na_stringu(tekst):
    """Usuwa wszystko oprócz cyfr i wyświetla co drugą cyfrę."""
    cyfry = ""
    for znak in tekst:
        if znak.isdigit():
            cyfry += znak
    print(cyfry[::2])

tekst = "W Roku Panskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalil dekret o 20%ej zniżce podatkow"
operacje_na_stringu(tekst)
#5
def szyfruj_tekst(tekst, klucz):
    """Szyfruje tekst przez zmniejszenie kodu ASCII o klucz."""
    zaszyfrowany = ""
    for znak in tekst:
      zaszyfrowany += chr(ord(znak) - klucz)
    return zaszyfrowany

tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz (liczbę do odjęcia od ASCII): "))
zaszyfrowany = szyfruj_tekst(tekst, klucz)
print(f"Zaszyfrowany tekst: {zaszyfrowany}")
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
#8
def czy_trojkat(a, b, c):
    return a + b > c and a + c > b and b + c > a

a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

if czy_trojkat(a, b, c):
    print("Tak, te liczby mogą być bokami trójkąta.")
else:
    print("Nie, te liczby nie mogą być bokami trójkąta.")
