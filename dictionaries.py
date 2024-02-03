# Python dictionaries are unordered collections of key-value pairs. 
# They are used to store and retrieve data efficiently, associating a key with a value. 
# Dictionaries are mutable, meaning they can be modified after creation

# Creating a Dictionary:
empty_dict = {}            # Empty dictionary

# Dictionary with key value pairs.

student = {'name': 'Alan', 'age': 26, 'grade': 'A'}

print(student['name'])                # Accessing values
print(student['age'])
print(student['grade'])

# Adding and Updating Elements:

student = {'name': 'Alan', 'age': 26, 'grade': 'A'}
student['location'] = 'Nairobi'         # Adding an element

student['name'] = 'Manuel'               # Updating an element

print(student)

# Deleting an element

student = {'name': 'Alan', 'age': 26, 'grade': 'A'}
#del student['age']                        # Removing a key-value pair
print(student)

grade = student.pop('grade')               # Removing and returning the value associated with a key
print(grade)


# Dictionary methods
# Dictionaries have several methods for common operations like getting keys, values, or key-value pairs.

# Getting keys, values, and items
student = {'name': 'Alan', 'age': 26, 'grade': 'A'}

# keys = student.keys()
# values = student.values()
# items = student.items()

# Iterating over keys
for key in student:
    print(key)

# Iterating over key-value pairs
for key, value in student.items():
    print(key, value)


squares = {x: x**2 for x in range(5)}
print(squares)
