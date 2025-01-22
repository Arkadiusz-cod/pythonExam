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
text = "W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 uchwalił dekret o 20% zniżce podatków"
cleaned_text = "".join(c for c in text if not c.isdigit() and not c.isspace())
result = cleaned_text[::-1][::4]
print("Wynik:", result)
#4
def szyfruj_tekst(text, przesuniecie):
    return "".join(chr(ord(c) - przesuniecie) for c in text)

tekst = input("Podaj tekst: ")
przesuniecie = int(input("Podaj przesunięcie: "))
print("Zaszyfrowany tekst:", szyfruj_tekst(tekst, przesuniecie))
#5
def my_max(a, b, c):
    return max(a, b, c)

print("Maksimum:", my_max(5, 2, 7))
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
