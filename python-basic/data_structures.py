# Topic: List, Tuple, Dictionary, Set

# Topic:- LIST (Mutable)
# Creating list
numbers = [10, 20, 30, 40]
names = ["Tirth", "Rahul", "Amit"]

print("Numbers:", numbers)
print("Names:", names)

# Accessing elements
print("First number:", numbers[0])
print("Last name:", names[-1])

# Modifying elements (Mutable)
numbers[1] = 25
names[0] = "Tirth Acharya"
print(numbers)
print(names)

# Adding elements
print("\n--- Adding Elements ---")
numbers.append(50)              # add at end
numbers.insert(1, 15)           # add at index
print(numbers)

# Removing elements
print("\n--- Removing Elements ---")
numbers.remove(25)              # remove value
numbers.pop()                   # remove last
numbers.pop(0)                  # remove by index
print(numbers)

# Looping through list
print("\n--- Looping ---")
for num in numbers:
    print(num)

# List length
print("\n--- Length ---")
print("Total elements:", len(numbers))

# Checking membership
print("\n--- Membership ---")
print(30 in numbers)
print(100 in numbers)

# Sorting list
print("\n--- Sorting ---")
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

# Copy list
print("\n--- Copy ---")
copy_numbers = numbers.copy()
print("Copied List:", copy_numbers)

# Clear list
print("\n--- Clear ---")
temp = [1, 2, 3]
temp.clear()
print(temp)

# List slicing
nums = [1, 2, 3, 4, 5]
print(nums[1:4])
print(nums[::-1])   # reverse

# Topic:- TUPLE (Immutable)
colors = ("red", "green", "blue", "yellow")
numbers = (10, 20, 30, 40, 50)
print("Colors Tuple:", colors)
print("Numbers Tuple:", numbers)

# Accessing elements (Indexing)
print("First color:", colors[0])
print("Last number:", numbers[-1])

# Slicing
print("colors[1:3]:", colors[1:3])
print("numbers[:3]:", numbers[:3])

# Looping through tuple
for i in colors:
    print(i)

# Checking membership
print("red" in colors)
print("black" in colors)

# Tuple length
print("Total colors:", len(colors))

# Nested tuple
student = ("Tirth", 22, ("Python", "Django"))
print(student)
print("Course:", student[2][0])

# Tuple unpacking
a, b, c, d = colors
print(a)
print(b)
print(c)
print(d)

# Converting list to tuple
list1 = [80, 85, 90]
tuple1 = tuple(list1)
print(tuple1)

# Converting tuple to list (to modify)
temp_list = list(numbers)
temp_list.append(60)
numbers = tuple(temp_list)
print(numbers)


# Topic: Dictionary (Key-Value Data Type)

# Creating dictionary
student = {
    "name": "Tirth",
    "age": 22,
    "course": "Python"
}
print("Student:", student)

# Accessing values
print("\n--- Accessing Values ---")
print("Name:", student["name"])
print("Age:", student.get("age"))        # safer access
print("City:", student.get("city", "Not Found"))

# Adding new key-value
print("\n--- Adding Data ---")
student["city"] = "Ahmedabad"
student["email"] = "tirth@gmail.com"
print(student)

# Updating existing value
print("\n--- Updating Data ---")
student["age"] = 23
print(student)

# Removing data
print("\n--- Removing Data ---")
student.pop("email")        # remove specific key
print(student)

student.popitem()           # remove last inserted item
print(student)

# Looping through dictionary
print("\n--- Looping ---")
for key in student:
    print(key, ":", student[key])

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Dictionary length
print("\n--- Length ---")
print("Total keys:", len(student))

# Checking key existence
print("\n--- Membership ---")
print("name" in student)
print("salary" in student)

# Nested dictionary
company = {
    "employee1": {"name": "Tirth", "role": "Developer"},
    "employee2": {"name": "Amit", "role": "Tester"}
}
print(company["employee1"]["name"])

# Copy dictionary
copy_student = student.copy()
print(copy_student)

# Clear dictionary
student.clear()
print(student)

# Topic: Set (Unordered & Unique Collection)

# Creating set
numbers = {10, 20, 30, 40, 40}
colors = {"red", "green", "blue"}

print("Numbers Set:", numbers)
print("Colors Set:", colors)

# Empty set (important)
empty_set = set()
print("Empty Set:", empty_set)

# Adding elements
print("\n--- Adding Elements ---")
numbers.add(50)
numbers.update([60, 70])
print(numbers)

# Removing elements
print("\n--- Removing Elements ---")
numbers.remove(20)      # error if not exists
numbers.discard(100)    # no error
print(numbers)

# Pop element (random)
print("\n--- Pop Element ---")
removed = numbers.pop()
print("Removed:", removed)
print(numbers)

# Membership check
print("\n--- Membership ---")
print(30 in numbers)
print(100 in numbers)

# Looping
print("\n--- Looping ---")
for num in numbers:
    print(num)

# Length
print("\n--- Length ---")
print("Total elements:", len(numbers))
print("\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)