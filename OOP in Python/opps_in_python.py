"""
To map with real world scenarios, we started using objects in code.
This is called object oriented programming. 


Object:- It is a real world entity.
        It is a container.
        => data -> attributes
        => functionality -> methods
"""

fruits = ["apple", "banana", "cherry", "mango"]
print(type(fruits))

# Fruit is an object of a class
fruits.append("orange")

"""
car1 
    => brand = "BMW", model = "XM", Year = 2026
    => accelerate, brake 

dot notation (.)

car1.brand => "BMW"
car1.accelerate(10)

"""

# Creating Objects => we need classes

# Classes => are like templates/blueprints/design used for creating objects
# classes also called as type

# Objects are created using the class and called as Instances of a class.
# Class will have all the details, attributes, functionality of the object.


"""
How to write classes name:-
    It can be using underscore: user_name, _user_name, etc
    It can be UserName,
    This two ways are standard to write a class name.
"""

# Creating a class

class MyClass: # It is an empty class with pass, so that it will not give an error. Making it syntactically correct.
    pass


# Creating a object we have to use class name
obj1 = MyClass()
obj2 = MyClass()

# obj1 and obj2 are objects of a class MyClass.

l1 = [10, 20, 30]
print(type(l1))


print(type(obj1)) # Output:- <class '__main__.MyClass'>
print(type(obj2)) # Output:- <class '__main__.MyClass'>


# Anything starting with double underscore and ending with double underscore then it will call as Dunder.

# Calling methods using objects?
# obj1.method(arg1,arg2,.....)



# Creating classes and objects.py

class Student:
    """
    This is a class Student to manage student information and activities.
    """
    pass

s1 = Student()
s2 = Student()

# Doc strings ==> it is the documentation about the class.
# How to know what is in docstring?
print(Student.__doc__)
print(help(Student))


