# Zadanie 1.1 - Obliczanie wyrażenia float dla podanej liczby naturalnej n
def zadanie_1_1():
    n = int(input("Podaj liczbę naturalną n: "))
    wynik = sum(i**2 + i**3 for i in range(1, n + 1))
    print(f"Wynik: {wynik}")

# Zadanie 1.2 - Pobieranie liczby całkowitej i wypisywanie jej cyfr w odwrotnej kolejności
def zadanie_1_2():
    liczba = int(input("Podaj liczbę całkowitą: "))
    while liczba > 0:
        print(liczba % 10, end='')
        liczba //= 10
    print()

# Zadanie 1.3 - Wyświetlenie co trzecią literę tekstu w odwrotnej kolejności
def zadanie_1_3():
    tekst = "W Roku Panskim 1345, wladca Henryk 12, na rzecz swoich 143209 poddanych znizyl podatki o 20%"
    tekst_bez_liter = ''.join(filter(str.isalpha, tekst))
    print(tekst_bez_liter[::-3])

# Zadanie 1.4 - Szyfrowanie tekstu poprzez zwiększenie kodu ASCII o wartość
def zadanie_1_4():
    tekst = input("Podaj tekst do zaszyfrowania: ")
    przesuniecie = int(input("Podaj wartość przesunięcia: "))
    zaszyfrowany = ''.join(chr(ord(znak) + przesuniecie) for znak in tekst)
    print(f"Zaszyfrowany tekst: {zaszyfrowany}")

# Zadanie 1.5 - Zwracanie maksimum z wartości bezwzględnych dwóch liczb
def zadanie_1_5(a, b):
    return max(abs(a), abs(b))

# Zadanie 1.6 - Zwracanie iloczynu kwadratów dowolnej ilości podanych liczb
def zadanie_1_6(*args):
    iloczyn = 1
    for liczba in args:
        iloczyn *= liczba**2
    return iloczyn

# Zadanie 1.7 - Suma cyfr liczby całkowitej (bez użycia string)
def zadanie_1_7():
    liczba = int(input("Podaj liczbę całkowitą: "))
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    print(f"Suma cyfr: {suma}")

# Zadanie 1.8 - Sprawdzanie, czy liczby są bokami trójkąta
def zadanie_1_8():
    while True:
        a, b, c = map(float, input("Podaj trzy liczby dodatnie: ").split())
        if a > 0 and b > 0 and c > 0:
            break
        print("Wszystkie liczby muszą być dodatnie!")
    if a + b > c and a + c > b and b + c > a:
        print("True")
    else:
        print("False")
