#gra rpg
class Character:
    def __init__(self, name, health, tactic_points):
        self.name = name
        self.health = min(max(health, 0), 100)  # Health between 0% and 100%
        self.tactic_points = tactic_points

    def change_health(self, amount):
        self.health = min(max(self.health + amount, 0), 100)

    def attack_power(self):
        raise NotImplementedError("Subclass must implement attack_power()")


class Archer(Character):
    def __init__(self, name, health, dexterity, tactic_points):
        super().__init__(name, health, tactic_points)
        self.dexterity = dexterity

    def attack_power(self):
        return self.dexterity * self.tactic_points * (self.health / 100)


class Warrior(Character):
    def __init__(self, name, health, strength, tactic_points):
        super().__init__(name, health, tactic_points)
        self.strength = strength

    def attack_power(self):
        multiplier = 1.5 if self.health < 20 else 1.0
        return self.strength * self.tactic_points * (self.health / 100) * multiplier


# Test RPG classes
archer = Archer("Robin", 80, 15, 10)
warrior = Warrior("Thor", 50, 20, 8)

print(f"{archer.name} Attack Power: {archer.attack_power()}")
print(f"{warrior.name} Attack Power: {warrior.attack_power()}")
warrior.change_health(-40)
print(f"{warrior.name} New Attack Power after Rage: {warrior.attack_power()}")

import random
even_file = "even.txt"
odd_file = "odd.txt"

with open(even_file,"w") as even, open(odd_file,"w") as odd:
    for _ in range(100):
        number = random.randint(-100,100)
        if number % 2 == 0:
            even.write(f"{number}\n")
        else:
            odd.write(f"{number}\n")
def calculate_sum_and_avg(file_name):
    with open(file_name,"r") as file:
        numbers = [int(line.strip()) for line in file]
        total = sum(numbers)
        avg = total / len(numbers) if numbers else 0
        return total,avg
even_sum,even_avg = calculate_sum_and_avg(even_file)
odd_sum,odd_avg = calculate_sum_and_avg(even_file)
print(f"Plik {even_file}: Suma = {even_sum}, Srednia = {even_avg}")
print(f"Plik {odd_file}: Suma = {odd_sum}, Srednia = {odd_avg}")

import requests

#wczytaj plik
import requests
url = "http://wmii.uwm.edu.pl/~muranova/WdPSt2024-25/DNA.txt"
response = requests.get(url)
dna_sequence = response.text.strip()

with open("DNA.txt","w") as file:
    file.write(dna_sequence)


#policz ile razy występuje w kodzie każda zasada azotowa - adenina, cytozyna,
guanina, tymina
adenine_count = dna_sequence.count('A')
cytosine_count = dna_sequence.count('C')
guanine_count = dna_sequence.count('G')
thymine_count = dna_sequence.count('T')
print(adenine_count,cytosine_count,guanine_count,thymine_count)

#Oczyść DNA z błędów typu N.
clean_dna_sequence = dna_sequence.replace('N', '').replace('-', '')
with open("DNA_cleaned.txt","w") as file:
    file.write(clean_dna_sequence)

#(d) Policz wystąpienia sekwencji GAGA
print(f"GAGA occurrences: {clean_dna.count('GAGA')}")

# Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu
index_7g = clean_dna_sequence.find('G' * 7)
    if index_7g != -1:
        print(index_7g)
    else:
        print("nie znaleziono")

#  Znajdź miejsce (indeks), gdzie od końca łańcucha występuje 6 cytozyn
reversed_index_6c = clean_dna_sequence[::-1].find('C' * 6)
    if reversed_index_6c != -1:
        actual_index_6c = len(clean_dna_sequence) - reversed_index_6c - 6
        print(actual_index_6c)
    else:
        print("nie znaleziono")

# Policz ile razy w kodzie pojawiła się sekwencja CTGAAA
ctgaaa_count = clean_dna_sequence.count('CTGAAA')

#  Uwzględnij wątpliwą ostatnią adeninę w CTGAAA
 pattern = re.compile(r'CTGAA.')
    matches = pattern.findall(clean_dna_sequence)
    print({len(matches)})

# Utwórz odpowiadającą nić RNA i zapisz do pliku
 rna_sequence = clean_dna_sequence('T','U')
    with open("RNA.txt", "w") as file:
        file.write(rna_sequence)
