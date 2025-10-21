class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started!")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car has an Engine

    def drive(self):
        self.engine.start()
        print(f"The {self.brand} is now driving!")

engine = Engine(200)
car = Car("Mercedes", engine)
car.drive()


