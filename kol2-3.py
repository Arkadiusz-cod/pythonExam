
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"{amount} transferred to {target_account.owner}.")

class PrivatAccount(Account):
    def salary_transfer(self, amount):
        self.deposit(amount)
        print(f"Salary of {amount} transferred to account.")

class FirmAccount(Account):
    def pay_taxes(self, amount):
        self.withdraw(amount)
        print(f"Paid taxes of {amount}.")

# Create accounts
account1 = PrivatAccount("John", 1000)
account2 = FirmAccount("Company Inc.", 5000)
account3 = Account("Alice", 2000)

# Perform some operations
account1.deposit(500)
account2.pay_taxes(1000)
account1.transfer(account3, 200)
account3.withdraw(300)

# Roman numeral class
class Roman:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, value):
        if isinstance(value, str):
            self.value = self._roman_to_int(value)
        elif isinstance(value, int):
            self.value = value

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __str__(self):
        return self._int_to_roman(self.value)

    @staticmethod
    def _roman_to_int(roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            curr_value = Roman.roman_map[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total

    @staticmethod
    def _int_to_roman(number):
        values = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
                  ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        result = ""
        for roman, value in values:
            while number >= value:
                result += roman
                number -= value
        return result

# Test Roman class
r1 = Roman("X")
r2 = Roman("V")
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)

# Vector class
class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.elements, other.elements)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.elements, other.elements)])

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.elements])

    def __str__(self):
        return str(self.elements)

# Test Vector class
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)

# Polynomial class
class Polynomial(Vector):
    def __str__(self):
        terms = []
        for i, coef in enumerate(reversed(self.elements)):
            if coef != 0:
                degree = len(self.elements) - i - 1
                if degree > 0:
                    terms.append(f"{coef}x^{degree}")
                else:
                    terms.append(f"{coef}")
        return " + ".join(terms)

    def degree(self):
        return len(self.elements) - 1

    def evaluate(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.elements))

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (len(self.elements) + len(other.elements) - 1)
            for i, coef1 in enumerate(self.elements):
                for j, coef2 in enumerate(other.elements):
                    result[i + j] += coef1 * coef2
            return Polynomial(result)

# Test Polynomial class
p1 = Polynomial([1, -1, 1, -2, 2])
p2 = Polynomial([1, 2])
print(p1)
print(p1.degree())
print(p1.evaluate(1))
print(p1 * p2)
