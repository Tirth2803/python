# Program 1: Single Inheritance (BASIC)

# Parent class
# class Animal:
#     def eat(self):
#         print("Animal eats food")

# # Child class
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.eat()    # Parent method
# d.bark()   # Child method


# class girls:
#     def brak(self):
#         print("khushi is braks")

# class khushi(girls):
#     def eat(self):
#         print("Tirth eating")

# k = khushi()
# k.eat()
# k.brak()

# Multilevel Inheritance

# class GrandFather:
#     def house(self):
#         print("Has a house")

# class Father(GrandFather):
#     def car(self):
#         print("Has a car")

# class Son(Father):
#     def bike(self):
#         print("has a bike")

# S = Son()
# S.house()
# S.bike()
# S.car()

# Multiple Inheritance

# class Father:
#     def skiils(self):
#         print("Driving")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class child(Father, Mother):
#     pass

# C = child()
# C.skills()

# class Father:
#     def skills(self):
#         print("Driving")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()
# c.skills()


# super() Keyword

class Parent:
   def show(self):
      print("Parent method")

class Child(Parent):
   def show(self):
      super().show()
      print("Child method")

c = Child()
c.show()