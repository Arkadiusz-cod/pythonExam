# Zadanie 2.1 - Rysowanie prostokąta z gwiazdek
def zadanie_2_1():
    n = int(input("Podaj wysokość prostokąta: "))
    m = int(input("Podaj szerokość prostokąta: "))
    for _ in range(n):
        print("*" * m)

# Zadanie 2.2 - Obliczanie wyrażenia float dla podanej liczby naturalnej n
def oblicz_wyrazenie(n):
    """Oblicza wartość wyrażenia a1^2 + a2^2 + ... + an^2."""
    suma = 0
    for i in range(n):
        a = float(input(f"Podaj liczbę a{i+1}: "))
        suma += a**2
    return suma

# Przykład użycia:
n = int(input("Podaj ilość liczb n: "))
wynik = oblicz_wyrazenie(n)
print(f"Wartość wyrażenia: {wynik}")

# Zadanie 2.3 - Wyświetlenie co drugą literę tekstu po usunięciu spacji
def operacje_na_stringu(tekst):
    """Usuwa litery i spacje, a następnie wyświetla co drugi znak."""
    nowy_tekst = ""
    for znak in tekst:
        if znak.isdigit():
            nowy_tekst += znak
    print(nowy_tekst[::2])

# Przykład użycia:
tekst = "W Roku Panskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalil dekret o 20%ej zniżce podatków!"
operacje_na_stringu(tekst)

# Zadanie 2.4 - Szyfrowanie tekstu poprzez przestawianie znaków
def zadanie_2_4():
    tekst = input("Podaj tekst do zaszyfrowania: ")
    zaszyfrowany = tekst[1:] + tekst[0]
    print(f"Zaszyfrowany tekst: {zaszyfrowany}")

# Zadanie 2.5 - Znajdowanie minimum z trzech liczb
def my_min(a, b, c):
    """Znajduje minimum z trzech liczb."""
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    return minimum

# Przykład użycia:
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))
minimum = my_min(a, b, c)
print(f"Minimum: {minimum}")

# Zadanie 2.6 - Zwracanie sumy kwadratów dowolnej ilości podanych liczb
def suma_kwadratow(*args):
    """Oblicza sumę kwadratów dowolnej ilości liczb."""
    suma = 0
    for liczba in args:
        suma += liczba**2
    return suma

# Przykład użycia:
wynik = suma_kwadratow(5, -1, 7)
print(f"Suma kwadratów: {wynik}")

# Zadanie 2.7 - Suma cyfr liczby całkowitej w odwrotnej kolejności (bez użycia string)
def zadanie_2_7():
    liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = 0
    while liczba > 0:
        wynik = wynik * 10 + (liczba % 10)
        liczba //= 10
    print(f"Liczba w odwrotnej kolejności: {wynik}")

# Zadanie 2.8 - Obliczanie pola koła
def pole_kola(a, litera):
    """Oblicza pole koła na podstawie promienia lub średnicy."""
    if litera == 'r':
        return math.pi * a**2
    elif litera == 'd':
        return math.pi * (a/2)**2
    else:
        return "Niepoprawna litera. Użyj 'r' dla promienia lub 'd' dla średnicy."

while True:
    litera = input("Podaj literę (r - promień, d - średnica): ")
    try:
        a = float(input("Podaj liczbę: "))
        if a < 0:
            print("Liczba musi być dodatnia.")
            continue
        break #przerwanie pętli jeśli dane są poprawne
    except ValueError:
        print("Niepoprawne dane. Podaj liczbę.")

wynik = pole_kola(a, litera)
print(f"Pole koła: {wynik}")
