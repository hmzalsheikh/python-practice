# Positional Arguments
def greet(name, language):
    print(f"Hello {name}, you’re learning {language}!")

greet("Hamzeh", "Python")

# Keyword Arguments
greet(language="Python", name="Hamzeh")


# Default Arguments
def greet(name="Friend", language="Python"):
    print(f"Hello {name}, you’re learning {language}!")

greet()               # Uses both defaults
greet("Hamzeh")       # Overrides the first
greet(language="C++") # Overrides the second


# Variable-Length Arguments
def add_numbers(*args): #for many positional arguments
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # 10

def introduce(**kwargs): #for many keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Hamzeh", age=31, hobby="Cycling")


# Return Values
def multiply(a, b):
    return a * b

result = multiply(5, 6)
print(result)


def stats(a, b):
    return a + b, a * b

sum_result, product_result = stats(3, 4)
print(sum_result, product_result)

# Exercise 1 – Default argument
def welcome_user(name="guest"):
    print(f"Welcome, {name}!")

welcome_user()


# Exercise 2 – Variable-length arguments
def average(*n):
    return sum(n)/len(n)
    
print(average(2, 4, 6, 8, 9, 5))



# Exercise 3 – Keyword arguments
def profile_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
              

profile_info(name="Hamzeh", age=31, location="berlin")


# Exercise 4 – Return multiple values
def min_max(*numbers):
    minmax = min(numbers), max(numbers)
    return minmax


print(min_max(2,5,7,8,3,6))

# Ex 4 (better way)
def min_max(*numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max(2,5,7,8,3,6)
print(f"Min: {smallest}, Max: {largest}")

#Bonus challenges

#Welcoming guests
def welcome_users(user_name = "Guest"):
    print(f"Welcome, {user_name}")


#Adding numbers
scores = [2, 5, 7, 15, 33, 25]
def add_nums(*scores):
    return sum(scores)


#Calculate min / max score
def calculate_minmax(*scores):
    return min(scores), max(scores)

lowest, highest = calculate_minmax(*scores)



#Calculate average
def scores_average(scores):
    return sum(scores)/len(scores)

score_average = scores_average(scores)


#Displaying all
welcome_users()
print(f"Min: {lowest}\n")
print(f"Max: {highest}\n")
print(f"Average: {score_average:.2f}")
