# Attributes in classes
# Attributes are defined using . notation
# Attributes are variables that belong to an object or a class.

class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "John"  # Here name and roll are instance attributes, They belong to only student1, not to the class Student and not to student2.
student1.roll = 101

print(student1.name)
print(student1.roll)

"""
print(student2.name) # AttributeError: 'Student' object has no attribute 'name'
print(student2.roll) # AttributeError: 'Student' object has no attribute 'name'
Why this gives and error?
=> student2 never received name or roll. Python does NOT automatically copy attributes between objects.
Each object maintains its own storage
"""

help(Student)
print(student1.__dict__) # Output:- {'name': 'John', 'roll': 101}  ==> This will store the variables or attribues we created or associated with the object
"""
__dict__ is a dictionary that stores all instance attributes
keys -> attribute name
values -> attribute values

Python stores all dynamically created attributes inside this dicitonary.
"""

