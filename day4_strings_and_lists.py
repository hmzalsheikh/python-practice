#Exercise 1 – String slicing
text = "python Programming"
print(text[:7])
print(text[-6::1])
print(text[::-1])

#Exercise 2 – String methods
message = " Hello world "
refined_msg = message.replace("world", "Python").strip().upper()

print(refined_msg)

#Exercise 3 – List methods
nums = [3, 1, 4, 1, 5]

nums.append(9)
print(nums)

nums.remove(1)
print(nums)

nums.sort()
print(nums)

nums.reverse()
print(nums)

#Exercise 4 – Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix [1][2])

for row in matrix:
    for item in row:
        print(item)