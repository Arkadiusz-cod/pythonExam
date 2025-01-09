import math
#Napisz funkcję, która sprawdza czy na liście elementy są posortowane od największych do najmniejszych (wtedy zwraca True, w przeciwnym wypadku
# False). Stwórz dwa przypadki testowe
def is_sorted_descending(lst):
 return lst == sorted(lst, reverse=True)
print(is_sorted_descending([5, 4, 3, 2, 1]))
print(is_sorted_descending([5, 4, 2, 3, 1]))
#Napisz funkcję, która sumuje dwa podanych lista jako wektory.
def sum_vectors(v1, v2):
    return [x + y for x,y in zip(v1, v2)]
    print(sum_vectors([1, 2, 3], [4, 5, 6]))
#Napisz funkcję func(list, n1, n2) która pobiera listę liczb typu int i za-
#mienia w całej liście liczbę n1 na liczbę n2, zwracając None.
def replace_in_place(lst, n1, n2):
    for i in range(len(lst)):
        if lst[i] == n1:
            lst[i] = n2
        return None
lst = [1, 2, 3, 1]
replace_in_place(lst, 1, 99)
print(lst)
#Napisz funkcję func(list, n1, n2) która pobiera listę liczb typu int i zwraca
#nowa lista, w której liczby n1 sa zamienione na n2.
def replace_and_return(lst, n1, n2):
    return [n2 if x == n1 else x for x in lst]
lst = [1, 2, 3, 1]
print(replace_and_return(lst, 1, 99))
#Zmodyfikuj funkcję tak żeby dziala na liczbach typu float, zmieniając na n2
#wszystkie liczby bliskie do n1 (isclose). Parametry isclose() muszą być
#parametrami funkcje
def replace_with_isclose(lst, n1, n2):
    return [n2 if math.isclose(x, n1) else x for x in lst]
print(replace_with_isclose([1.0, 1.00001, 2.0],1.0, 99.0))
#Posortuj listę zawierająca nazwy miesięcy kalendarzowych za pomocą funkcje
#sort(). https://www.w3schools.com/python/ref_list_sort.asp
#Wskazówka Napisz funkcję, która zwraca numer miesiąca po nazwie
    months = ["Marzec", "Grudzień", "Luty", "Styczeń", "Listopad", "Wrzesień", "Maj", "Październik", "Czerwiec", "Sierpień", "Lipiec", "Kwiecień"]
    months.sort()
    print(months)
#Krotki (tuples)). (a) stwórz krotkę o 7 elementach różnych typów.
#Spróbuj zmienić element o indeksie 2. Wyświetl na konsoli element krotki o
#indeksie 3. Wyświetl na konsoli elementy krotki o indeksach 3,4,5 w jednym
#poleceniu. Wyświetl na konsoli element trzeci od końca
tup = (10, "tekst", 3.14, True, [1,2], (3, 6), None)
print(tup[3])
print(tup[3:6])
print(tup[-3])
#Napisz funkcję, której parametrom jest krotka i element, a wynikiem – krotką
#z dodanym elementem (2 możliwości). Zrób to samo z usunięciem elementu.
def add_to_tuple(tup, element):
    return tup + (element,)
print(add_to_tuple(tup,"element"))
def remove_from_tuple(tup, element):
    return tuple(x for x in tup if x != element)
print(remove_from_tuple(tup, True))
#ypisz piątę potęgę liczb od 0 do 14 naturalnych jako listę
powers_of_five = [x**5 for x in range(15)]
print(powers_of_five)
#Wypisz silnię pierwszych 10 liczb naturalnych jako listę.
import math
factorials = [math.factorial(x) for x in range(10)]
print(factorials)
#1, e1, e2, e3, . . . e9 jako listę
import math
exponentials = [math.exp(x) for x in range(10)]
print(exponentials)
#Utwórz listą nazwisk i wybierz ze stworzonej listy nazwisk nazwiska, których długość jest większa niż 6 symbolów.
names = ["Kowalski","Nowak","Dąbrowski","Wójcik"]
long_names = [names for names in names if len(names) > 6]
print(long_names)
#Napisz funkcję, która zwraca elementy parzysty ciągu wejściowego, podnie- sione do trzeciej potęg
def even_cubed(lst):
    return [x**3 for x in lst if x % 2 == 0]
print(even_cubed([1, 2, 3, 4, 5, 6]))
# Dla poniższej zmiennej names:
#names = ["michal", "nela", "ola", "przemek"]
#(a) policz sumaryczną długość wszystkich tych imion.
#(b) stwórz listę, w której wszystkie te imiona zaczynają się wielką literą (przypomnij sobie metody z klasy str),3
#(c) stwórz listę, w którym znajdują się wyłącznie te imiona, w których jest litera “l”.
#(d) stwórz tuple, w którym znajdują się wyłącznie żeńskie imiona, zaczynające
#się wielką literą (żeńskie imiona to te kończące się na “a”)
names = ["michal","nela","ola","przemek"]
total_length = sum(len(names) for names in names)
print(total_length)

capitalized_names = [names.capitalize() for names in names]
print(capitalized_names)

names_with_l = [names for names in names if "l" in names]
print(names_with_l)

female_names = tuple(names.capitalize() for names in names if names.endswith('a'))
print(female_names)

