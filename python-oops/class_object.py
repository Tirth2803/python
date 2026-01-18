# Topic: Class and Object in Python

# Defining a class
class Student:
    # class variables
    college = "ABC Institute"

     # method
    def display(self):
        print("College:", Student.college)

# Creating objects of class
s1 = Student()
s2 = Student()

# Calling method using object
s1.display()
s2.display()


class Demo:
    def __init__(self):
        print("Default Constructor")


# Constructor + Class Variable

class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary, Employee.company)

e1 = Employee("Amit", 50000)
e2 = Employee("Neha", 60000)

e1.display()
e2.display()