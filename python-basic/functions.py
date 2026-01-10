# Topic: Functions

# Function without return
def greet(name):
    print("Hello", name)
greet("Tirth")
greet("Khushi")

# Function with return
def add(a, b):
    return a + b
result = add(10, 20)
print("Addition:", result)


# Default parameter
def country(name, country="India"):
    print(name, "is from", country)
country("Tirth")
country("Rahul", "USA")