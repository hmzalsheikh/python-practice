# Exercise 1 – Loop through a list
# Assign fruits list
fruits = ["mango", "pineapple", "melon"]

# For loop
for fruit in fruits:
    print("I like, ", fruit)

# Exercise 2 – Sum numbers in a list
# Assign numbers list
numbers = [2, 4, 6, 8, 10]
total = 0

# For Loop/ adding all nums
for num in numbers:
    total += num

# Display the total
print("Total: ", total)

# Exercise 3 – Use a while loop
# Use a while loop
count = 5
while count > 0:
    print("countdown: ", count) # Displays numbers over 0
    count -= 1 # After displaying previous number takes away 1 and loops back until hits 0
print("Blast off!") # After hitting 0 displays blast off!

# Exercise 4 – Combine loops + conditionals
# Assign a numbers list
numbers = [1, 2, 3, 4, 5, 6]

# use a for loop
for num in numbers:
    if num % 2 == 0: #use a conditional
        print(num, "is even")
    else:
        print(num, "is odd")