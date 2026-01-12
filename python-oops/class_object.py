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