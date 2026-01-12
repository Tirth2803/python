# Topic: Exception Handling

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Result:", a / b)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

# except ValueError:
#     print("Error: Invalid input")


# Multiple except blocks

# try:
#     x = int(input("Enter number: "))
#     y = int(input("Enter number: "))
#     print(x / y)

# except ZeroDivisionError:
#     print("Division by zero error")

# except ValueError:
#     print("Please enter numbers only")

# except Exception as e:
#     print("Unknown error:", e)

# Exception → parent class of all errors

# try–except–else

# try:
#     num = int(input("Enter number: "))
#     print("Square:", num * num)

# except ValueError:
#     print("Invalid input")

# else:
#     print("Program executed successfully")

# try–except–finally (IMPORTANT)

# try:
#     file = open("data.txt", "r")
#     print(file.read())

# except FileNotFoundError:
#     print("File not found")

# finally:
#     print("Execution completed")

# try:
#     file = open("user.txt","r")
#     print(file.read())

# except FileNotFoundError:
#     print("File not found")

# finally:
#     print("Execution completed")

# finally always runs (cleanup)

# Raising Custom Exception

# age = int(input("Enter age: "))

# if age < 18:
#     raise ValueError("Age must be 18 or above")
# print("Eligible for vote")

# User-Defined Exception (Advanced)

# class NegativeNumberError(Exception):
#     pass

# try:
#     num = int(input("Enter positive number: "))
#     if num < 0:
#         raise NegativeNumberError("Negative number not allowed")

#     print("Valid number")

# except NegativeNumberError as e:
#     print(e)


# Exception Handling with File Handling

try:
    with open("users.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("Permission denied")