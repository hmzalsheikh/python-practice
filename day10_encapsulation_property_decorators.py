# encapsulation and @property in action

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    # Getter — lets us *read* the balance safely
    @property
    def balance(self):
        return self.__balance

    # Setter — lets us *update* the balance safely
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("❌ Balance cannot be negative!")
        else:
            self.__balance = amount

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount}. New balance: {self.__balance}")
        else:
            print("❌ Deposit amount must be positive!")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"💸 Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("❌ Insufficient funds!")


# --- Testing the class ---
account = BankAccount("Hamzeh", 1000)

print(account.balance)     # ✅ Access using property (no parentheses)
account.deposit(500)       # Deposit money
account.withdraw(200)      # Withdraw money
account.balance = -100     # ❌ Invalid
account.balance = 3000     # ✅ Works
print(account.balance)     # ✅ Updated safely


# Challenge

class FitnessTracker:
    def __init__(self, steps, distance, calories):
        self.__steps = steps
        self.__distance = distance
        self.__calories = calories

    @property
    def steps(self):
        return self.__steps
    
    @steps.setter
    def steps(self, count):
        if count < 0:
            print("Step count cant be negative")
        else:
            self.__steps = count

    def add_steps(self, amount):
        if amount > 0:
            self.__steps += amount
            print(f"{amount} added to your log. todays step count {self.__steps}")
        else:
            print("Steps must be positive")

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, amount):
        if amount < 0:
            print("Distance cant be negative")
        else:
            self.__distance = amount
    
    @property
    def calories(self):
        return self.__calories
    
    @calories.setter
    def calories(self, amount):
        if amount < 0:
            print("Calories cant be negative")
        else:
            self.__calories = amount

    def add_calories(self, amount):
        if self.__calories > 0:
            amount = int(self.__steps / 200)
            self.__calories += amount
            print(f"{amount} calories burned. todays calorie count {self.__calories}")
        else:
            print("calories must be positive")

    def summary(self):
        print(f"Today's Summary:\n"
              f"Steps: {self.__steps}\n"
              f"Distance : {self.__distance} km\n"
              f"Calories burned : {self.__calories}")


fitness = FitnessTracker(4000, 5, 400)

fitness.summary()
fitness.add_steps(200)
fitness.add_calories(150)
fitness.add_steps(-300)


    

