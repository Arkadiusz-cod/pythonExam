#(Zbiory (set)). (a) stwórz zbiór (set) z 5 nazwami Państw
#• spróbuj dodać do zbioru istniejące element w zbiorze
#• sprawdź, czy Polska jest w zbiorze
#• usuń ze zbioru istniejący element
from calendar import month
from distutils.command.install import value
from os.path import defpath

countries = {"Polska","Niemcy","Francja","Hiszpania","Włochy"}
countries.add("Polska")
print("Polska jest w zbiorze", "Polska" in countries)
countries.remove("Hiszpania")
print("Zbior po usunieciu Hiszpanii", countries)
 #stwórz dwa zbiory z nazwami miast. Wyświetl:
#• miasta, które są w przynajmniej jednym ze zbiorów (odpowiednik sumy
#zbiorów),
#• miasta, które są jednoczesne we wszystkich zbiorach (odpowiednik części
#wspólnej zbiorów),
#• miasta, które są w pierwszym zbiorze, ale nie ma ich w drugim zbiorze
#(odpowiednik różnicy zbiorów),
#• wyszukaj sposoby sprawdzenia czy zbiór x jest podzbiorem zbioru y.
#Sprawdź na przykładzie zbiorów miast.
cities_1 = {"Warszawa","Berlin","Paryż","Rzym"}
cities_2 = {"Berlin","Londyn","Paryż","Madryt"}
print("Miasta w przynajmniej jednym zbiorze: ", cities_1 | cities_2)
print("Miasta jednocześnie w obu zbiorach", cities_1 & cities_2)
print("Miasta w pierwszym zbiorze, ale w drugim nie", cities_1 - cities_2)
print("Czy cities_1 jest podzbiorem cities_2: ", cities_1.issubset(cities_2))
print("Czy cities_2 jest podzbiorem cities_1: ", cities_2.issubset(cities_1))
# 2 (Słownik (dictionary)). (a) • Stwórz słownik , który będzie przechowywał jako klucz imiona, a jako wartość jakieś liczby (odpowiadające
#numerom telefonu). Następnie wykonaj kilka operacji na słowniku.
#• Napisz funkcją print_phone_numbers, która wypisuje na konsoli dla podanego slownika wszystkie numery w postaci
#...(Imie Nazwisko)... ma numer ...()....
#(b) • Napisz funkcję, która zamienia podaną listą dni tygodnia angielskimi odpowiednikami i funkcję odwrotną.
#• Napisz funkcję, która posortuje listę zawierająca nazwy miesięcy kalendarzowych przy pomocy słownika.
#• Napisz funkcję, która jako parametr pobiera liczbę w systemie rzymskim
#(typ string), a zwraca wartość liczby w systemie arabskim.
#https://pl.wikipedia.org/wiki/Rzymski_system_zapisywania_liczb
#• Napisz odwrotną funkcję, której parametrom jest liczba arabska, a wynikiem – liczba rzymska (nie obowiązkowo używać słownik)
phone_book = {
    "Anna": "123-456-789",
    "Jan": "987-654-321",
    "Maria": "555-666-777"
}
def print_phone_numbers(phone_dict):
    for name, number in phone_dict.items():
        print(f"{name} ma numer {number}")
print_phone_numbers(phone_book)

polish_to_english_days = {
    "poniedziałek": "Monday",
    "wtorek": "Tuesday",
    "środa": "Wednesday",
    "czwartek": "Thursday",
    "piątek": "Friday",
    "sobota": "Saturday",
    "niedziela": "Sunday"
}
english_to_polish_days = {v: k for k, v in polish_to_english_days.items()}
def translate_days_to_english(days):
    return [polish_to_english_days[day] for day in days]
def translate_days_to_polish(days):
    return [english_to_polish_days[day] for day in days]

month_order = {
    "Styczeń": 1, "Luty": 2, "Marzec": 3, "Kwiecień": 4,
    "Maj": 5, "Czerwiec": 6, "Lipiec": 7, "Sierpień": 8,
    "Wrzesień": 9, "Październik": 10, "Listopad": 11, "Grudzień": 12
}
def sort_months(months):
    return sorted(months, key=lambda month: month_order[month])

roman_to_arabic = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}
def roman_to_int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_arabic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
            return total

        def int_to_roman(num):
            arabic_to_roman = [
                (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
            ]
            result = ""
            for value, roman in arabic_to_roman:
                while num >= value:
                    result += roman
                    num -= value
            return result
print("Rzymska liczba 'XIV' to:", roman_to_int("XIV"))
print("Arabska liczba 14 to rzymska:", int_to_roman(14))
