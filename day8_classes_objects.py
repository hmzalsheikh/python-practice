# Exercise 1 – Create a simple class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)
print(my_dog.breed)


# Exercise 2 – Add a method (behavior)
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()


# Exercise 3 – Class with multiple methods
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))


# Exercise 4 – Class with attributes + methods
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

account1 = BankAccount("Hamzeh", 100)
account1.deposit(50)
account1.withdraw(30)
account1.withdraw(200)


# Challenge
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def car_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}")

    def age(self):
        from datetime import datetime, timedelta
        car_year = int(self.year)
        now = datetime.now().year

        car_age = now - car_year
        print(f"Car age: {car_age} years old")


car1 = car("Toyota", "Corolla", 2020)
car1.car_info()
car2 = car("Mercedes", "E63", 2013)
car2.car_info()

car1.age()
car2.age()
