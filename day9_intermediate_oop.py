# Inheritance

# Parent class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def car_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}")

# Child class
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)  # inherit from Car
        self.battery_size = battery_size
    
    def battery_info(self):
        print(f"{self.model} has a {self.battery_size}-kWh battery")

my_electric = ElectricCar("Tesla", "Model 3", 2021, 75)
my_electric.car_info()
my_electric.battery_info()


# Encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

acc = BankAccount("Hamzeh", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500


# Polymorphism

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()  # works for both Dog and Cat


# Challenge

from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def vehicle_info(self):
        print(f"This car is a {self.year} {self.color} {self.brand}")

    def age(self):
        age = datetime.now().year - int(self.year)
        print(f"{self.brand} is {age} years old.")

class Car(Vehicle):
    def __init__(self, brand, year, color, doors):
        super().__init__(brand, year, color)
        self.doors = doors

    def car_info(self):
        print(f"It has {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, year, color, type):
        super().__init__(brand, year, color)
        self.type = type

    def bike_info(self):
        print(f"This bike is a {self.year} {self.color} {self.type} {self.brand}")


my_car = Car("mercedes", 2022, "black", "2 doors")
my_bike = Bike("unknown bike", 2023, "silver", "city")

my_car.vehicle_info()
my_car.age()
my_car.car_info()
my_bike.bike_info()
my_bike.age()


# Challenge 2

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def info(self):
        print(f"This is {self.name}, a {self.age}-year-old {self.species}.")

    def birthday(self):
        bday = self.age + 1
        print(f"Happy birthday {self.name}! you're now {bday} years old! 🎉")

class Dog(Pet):
    def __init__(self, name, species, age, breed):
        super().__init__(name, species, age)
        self.breed = breed

    def bark(self):
        print(f"woof! {self.breed}")

class Cat(Pet):
    def __init__(self, name, species, age, color):
        super().__init__(name, species, age)
        self.color = color

    def meow(self):
        print(f"Meow! {self.color}")

my_pet = Pet("Seuss", "cat", 8)
my_dog = Dog("Rick", "dog", 5, "🐶")
my_cat = Cat("Seuss", "cat", 8, "🐱")

my_pet.info()
my_pet.birthday()
my_dog.bark()
my_cat.meow()