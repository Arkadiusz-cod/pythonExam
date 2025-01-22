# Zadanie 2.1 - Rysowanie prostokąta z gwiazdek
def zadanie_2_1():
    n = int(input("Podaj wysokość prostokąta: "))
    m = int(input("Podaj szerokość prostokąta: "))
    for _ in range(n):
        print("*" * m)

# Zadanie 2.2 - Obliczanie wyrażenia float dla podanej liczby naturalnej n
def zadanie_2_2():
    n = int(input("Podaj liczbę naturalną n: "))
    wynik = sum(i**2 + i**3 for i in range(1, n + 1))
    print(f"Wynik: {wynik}")

# Zadanie 2.3 - Wyświetlenie co drugą literę tekstu po usunięciu spacji
def zadanie_2_3():
    tekst = "W Roku Panskim 1345, wladca Henryk 12, na rzecz swoich 143209 poddanych znizyl podatki o 20%"
    tekst_bez_spacji = tekst.replace(" ", "")
    print(tekst_bez_spacji[1::2])

# Zadanie 2.4 - Szyfrowanie tekstu poprzez przestawianie znaków
def zadanie_2_4():
    tekst = input("Podaj tekst do zaszyfrowania: ")
    zaszyfrowany = tekst[1:] + tekst[0]
    print(f"Zaszyfrowany tekst: {zaszyfrowany}")

# Zadanie 2.5 - Znajdowanie minimum z trzech liczb
def zadanie_2_5(a, b, c):
    return min(a, b, c)

# Zadanie 2.6 - Zwracanie sumy kwadratów dowolnej ilości podanych liczb
def zadanie_2_6(*args):
    return sum(x**2 for x in args)

# Zadanie 2.7 - Suma cyfr liczby całkowitej w odwrotnej kolejności (bez użycia string)
def zadanie_2_7():
    liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = 0
    while liczba > 0:
        wynik = wynik * 10 + (liczba % 10)
        liczba //= 10
    print(f"Liczba w odwrotnej kolejności: {wynik}")

# Zadanie 2.8 - Obliczanie pola koła
def zadanie_2_8():
    import math
    while True:
        dane = input("Podaj 'r X' (promień) lub 'd X' (średnica): ").split()
        if len(dane) == 2 and dane[0] in ('r', 'd'):
            typ, wartosc = dane[0], float(dane[1])
            if wartosc > 0:
                if typ == 'r':
                    pole = math.pi * wartosc**2
                else:
                    pole = (math.pi / 4) * wartosc**2
                print(f"Pole koła: {pole}")
                break
        print("Niepoprawne dane. Spróbuj ponownie!")
