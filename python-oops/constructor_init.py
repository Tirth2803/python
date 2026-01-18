class Student:
    def __init__(self):
        print("Constructor called")

s1 = Student()

# Constructor with Parameters

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Tirth", 22)
s1.show()