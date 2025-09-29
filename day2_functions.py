def say_hello(name):
    return f'hello, {name}'

print(say_hello("Hamzeh"))
print(say_hello('Jael'))

#1. Factorial function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5)) # should print 120

#2. Palindrome checker
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('madam')) # True
print(is_palindrome('ham')) # False
    
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 7)) # 12