# Exercise 1 – Write to a file
with open("notes.txt", "w") as file:
    file.write("learning python is fun!")


# Exercise 2 – Read from the same file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


# Exercise 3 – Handle file not found
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found, please check the filename.")


 # Exercise 4 – Combine both
 #creating a file and displaying it, "w" writes and rewrites existing files
with open("user_input.txt", "w") as file:
    file.write(input("Write your input here: "))


with open("user_input.txt", "r") as file:
    content = file.read()
    print(content)

#creating a file and displaying with "x" that does not re-writes files
try:
    with open("pythonfile.txt", "x") as file:
        file.write(input("Write your input here: "))
except FileExistsError:
    print("Error, this file already exists!")

# Bonus challenge
from datetime import date

entry = input("Write your journal entry: ")

with open("Journal.txt", "a") as file:
    today = date.today()
    file.write(f"[{today}] {entry}\n")
    print("Your entry has been saved!")

print("\nHere's your journal so far:\n")
with open("Journal.txt", "r") as file:
    print(file.read())



