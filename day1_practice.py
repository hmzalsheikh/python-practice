# 1. Reverse a string
word = "developer"
print(word[::-1])  # expected output: repoleved

# 2. Count vowels in a word
word = "education"
vowels = "aeiou"
count = sum(1 for char in word if char in vowels)
print("Vowel count:", count)  # expected output: 5

# 3. Sum all numbers in a list
numbers = [2, 4, 6, 8, 10]
print("Sum:", sum(numbers))  # expected output: 30
