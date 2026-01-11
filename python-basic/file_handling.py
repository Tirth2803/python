# step:-1 OPEN & WRITE FILE

# Topic: File Handling - Write

file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("This is file handling example\n")
file.close()

print("Data written successfully")

# step2:- READ FILE (FULL)

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Read line by line

file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()

# step3:- APPEND FILE (ADD DATA)

file = open("data.txt", "a")
file.write("This line is appended\n")
file.close()

# step4:- BEST PRACTICE – with STATEMENT

with open("info.txt", "w") as file:
    file.write("Using with statement\n")
    file.write("File auto close")

with open("info.txt", "r") as file:
    print(file.read())

# step5:- FILE READ METHODS

with open("data.txt", "r") as file:
    print(file.read())       # all content

with open("data.txt", "r") as file:
    print(file.readline())   # single line
    print(file.readline())   # single line

with open("data.txt", "r") as file:
    print(file.readlines())  # list of lines

# step6:- REAL-WORLD EXAMPLE (User Data Save)

# name = input("Enter name: ")
# email = input("Enter email: ")

# with open("users.txt", "a") as file:
#     file.write(f"Name: {name}, Email: {email}\n")

# print("User saved successfully")

# step7:- FILE + LIST (IMPORTANT)

students = ["Tirth", "Amit", "Rahul"]

with open("students.txt", "w") as file:
    for s in students:
        file.write(s + "\n")

with open("students.txt", "r") as file:
    data = file.read().splitlines()
    print(data)


# FILE HANDLING + EXCEPTION (SAFE WAY)

try:
    with open("demo.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")