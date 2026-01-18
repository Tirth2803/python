# Public Members Example

# class User:
#     def __init__(self, name):
#         self.name = name # public variable
    
#     def show(self):
#         print("Name:",self.name)

# u = User("Tirth")
# u.show()
# print(u.name)
# u = User("Khushi")
# u.show()
# print(u.name)


# Protected Members Example

# class user:
#     def __init__(self):
#         self._age = 25

# class Student(user):
#     def show_age(self):
#         print("Age:", self._age)

# s = Student()
# s.show_age()
# print(s._age)

# Private Members (Real Encapsulation)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(10000)