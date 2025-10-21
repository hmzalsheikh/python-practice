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

from datetime import date

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
        
    def ret_summary(self):
        print(f"{date} Summary:\n"
              f"Steps: {self.__steps}\n"
              f"Distance : {self.__distance} km\n"
              f"Calories burned : {self.__calories}")
    

class WeeklyTracker:
    def __init__(self):
        self.records = []

    def add_day(self, fitness_obj):
        """Adds one day's record to the weekly tracker."""
        entry_date = date.today().strftime("%A, %d %b %Y")
        self.records.append({
            "date": entry_date,
            "steps": fitness_obj.steps,
            "distance": fitness_obj.distance,
            "calories": fitness_obj.calories
        })
        print(f"✅ Added log for {entry_date}\n")

    def weekly_summary(self):
        """Calculates total steps, distance, and calories for the week."""
        total_steps = sum(day["steps"] for day in self.records)
        total_distance = sum(day["distance"] for day in self.records)
        total_calories = sum(day["calories"] for day in self.records)

        print("\n--- 🗓️ Weekly Summary ---")
        for record in self.records:
            print(f"{record['date']} → {record['steps']} steps, "
                  f"{record['distance']} km, {record['calories']} cal")

        print("\nTotals:")
        print(f"Steps: {total_steps}")
        print(f"Distance: {total_distance} km")
        print(f"Calories: {total_calories}")
        print("--------------------------\n")


if __name__ == "__main__":
    # Create daily logs
    monday = FitnessTracker(4000, 3.5, 200)
    tuesday = FitnessTracker(7500, 6.2, 350)
    wednesday = FitnessTracker(9000, 7.5, 420)

    # Create a weekly tracker and add days
    week = WeeklyTracker()
    week.add_day(monday)
    week.add_day(tuesday)
    week.add_day(wednesday)

    # Display results
    week.weekly_summary()




    

