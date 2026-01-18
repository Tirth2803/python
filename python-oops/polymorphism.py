print(len("Python"))
print(len([1, 2, 3, 4]))
print(len((10, 20)))

# Operator Overloading

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])

# Method Overriding (Runtime Polymorphism)

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()
# d.sound()
# c.sound()

# Duck Typing (VERY IMPORTANT)

# class Dog:
#     def speak(self):
#         print("Bark")

# class Human:
#     def speak(self):
#         print("Hello")

# def call_speak(obj):
#     obj.speak()

# call_speak(Dog())
# call_speak(Human())

# Polymorphism with Function Arguments

class India:
    def capital(self):
        print("New Delhi")

class USA:
    def capital(self):
        print("Washington DC")

def show_capital(country):
    country.capital()

show_capital(India())
show_capital(USA())

# How Python handles Overloading?

class Test:
    def add(self, a, b, c=0, d=0):
        print(a + b + c + d)

t = Test()
t.add(2, 3)
t.add(2, 3, 4)
t.add(2,3,4,5)

# Real-Life Example (Payment System)

class Payment:
    def pay(self):
        print("Payment method")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")