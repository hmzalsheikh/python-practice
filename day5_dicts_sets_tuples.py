# Exercise 1 – Create and Access a Dictionary
#create a dictionary
person = {
    "name" : "Hamzeh",
    "age" : 31,
    "city" : "Berlin"
}

#access values
print(person["name"]) #“Give me this key or I’ll break.”
print(person.get("age")) 
#“Give me this key, or if it’s missing, I’ll handle it gracefully.”

# add a new key-value pair
person["profession"] = "Developer"

#loop through dictionary
for key,value in person.items():
    print(key, ":", value)

# Exercise 2 – Using Sets
#create two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#find common elements
print("Intersections: ", set_a & set_b)

#combine both sets
print("Union: ", set_a | set_b)

#difference (items in set_a but not in set_b)
print("Difference: ", set_a - set_b)

#Exercise 3 – Tuples and Immutability
#create a tuple
dimensions = (1920,1080)

#access elements
print("Width: ", dimensions[0])
print("Height: ", dimensions[1])

# Try to modify (will raise an error if uncommented)
# dimensions[0] = 1280

#tuple unpacking
width, height = dimensions
print(f"The resolutions is: {width}x{height}")

#Bonus - Convert between types
# Convert a list to a set to remove duplicates
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = list(set(numbers)) #converting a list → a set → back to a list.
#coverting to set removes duplicates automatically
print(unique_numbers)

# Convert a tuple to a list and modify it
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
my_list.append(40)
print(my_list)


profile = {
    "name" : "Hamzeh",
    "age" : 31,
    "skills" : ["Python", "Git", "Python", "Cybersecurity"]
}

print(profile["name"])
print(profile.get("city", "unknown"))
skills = profile["skills"]
new_list = list(set(skills))
print("New List: ", new_list)