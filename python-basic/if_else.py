# if-else example

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("zero")

# exaple2

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Your Grade:", grade)


# Nested if example
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")