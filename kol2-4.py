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

# Part (a): Generate numbers and save to files
even_file = "even.txt"
odd_file = "odd.txt"

with open(even_file, "w") as even, open(odd_file, "w") as odd:
    for _ in range(100):
        number = random.randint(-100, 100)
        if number % 2 == 0:
            even.write(f"{number}\n")
        else:
            odd.write(f"{number}\n")

# Part (b): Read files and calculate sum and average
def calculate_stats(filename):
    with open(filename, "r") as file:
        numbers = [int(line.strip()) for line in file]
        total = sum(numbers)
        average = total / len(numbers) if numbers else 0
        return total, average

even_stats = calculate_stats(even_file)
odd_stats = calculate_stats(odd_file)

print(f"Even - Sum: {even_stats[0]}, Average: {even_stats[1]}")
print(f"Odd - Sum: {odd_stats[0]}, Average: {odd_stats[1]}")

import requests

# (a) Load DNA
url = "http://wmii.uwm.edu.pl/~muranova/WdPSt2024-25/DNA.txt"
dna_file = "DNA.txt"
response = requests.get(url)
with open(dna_file, "w") as file:
    file.write(response.text.strip())

with open(dna_file, "r") as file:
    dna = file.read().strip()

# (b) Count occurrences of each nitrogen base
from collections import Counter

counts = Counter(dna)
print(f"Adenine: {counts['A']}, Cytosine: {counts['C']}, Guanine: {counts['G']}, Thymine: {counts['T']}")

# (c) Clean DNA
clean_dna = dna.replace("N", "").replace("-", "")
print(f"Clean DNA Length: {len(clean_dna)}")

# (d) Count GAGA
print(f"GAGA occurrences: {clean_dna.count('GAGA')}")

# (e) Index of 7 consecutive G
index_7g = clean_dna.find("G" * 7)
print(f"Index of 7 consecutive G: {index_7g}")

# (f) Index of last 6 consecutive C
index_6c = clean_dna.rfind("C" * 6)
print(f"Index of last 6 consecutive C: {index_6c}")

# (g) Count CTGAAA
print(f"CTGAAA occurrences: {clean_dna.count('CTGAAA')}")

# (h) Count CTGAAA with last A mutated
import re
pattern = "CTGAA[A|N|-]"
print(f"Mutated CTGAAA occurrences: {len(re.findall(pattern, clean_dna))}")

# (i) Create RNA sequence
rna = clean_dna.replace("T", "U")
rna_file = "RNA.txt"
with open(rna_file, "w") as file:
    file.write(rna)
print(f"RNA saved to {rna_file}")
