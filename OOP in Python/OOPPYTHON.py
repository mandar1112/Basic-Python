# OOPs in Python

# To map with real world scenarios, we started usign objects in code.
# This is called Object Oriented Programming.


# Class in Python
# A class is a collection of objects. Class is a blueprint for creating objects. 

# Object in Python
# An object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

# self Parameter :-  Seld parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

# __init__ Method:- it is the Constructor in Python, automatically called when a new object is created. It initializes the attributes(data, varialbes, etc) of the class.


# Class Variables:- These are the variables that are shared across all instances of a class. It is defined at the class level, outside any method.
# All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Variable:- Variables that are unique to each instance(object) of a classs. These are defined within the __init__ method or other instance methods.
# Each object maintains its own copy of the instance variables, independent of other objects.

# If Initialized method is not pass then python make a default constructor.


# Methods:- Methods are functions that belong to objects

# Instance Methods:- Methods that uses intance properties

# Static Methods:- Methods that don't use the self parameters (work at class level)
# It is denoted by @staticmethods. This is called as decorator. 

# Class Methods:- A class method is bound to the class & receives the class as an implicit first argument.
# Note:- Static Method can't access or modify class state & generally for utility.
# It is denoted by @classmethods. This is called as decorator. 


# creating class
class Student:
    
    college_name = "ABC College" # Class Attributes:- These are common for every object in the class
    

    # Python allows only one Constructor in one class otherwise it will overloading
    # Default Constructor
    #   def __init__(self):
    #       pass

    # Parameterized Constructor
    def __init__(self, name = None, marks = None):
        self.name = name # Here self is reference for the object
        self.marks = marks
        print("Adding New Student in Databases...")


    @classmethod
    def change_college_name(cls, college_name):
        # Student.college_name = college_name  # if not @classmethod is not given
        # self.__class__.college_name = college_name    # if not @classmethod is not given, this is another way
        cls.college_name = college_name # By using @classmethod
    

    # Instance Method
    def welcome(self):
        print(f"Welcome Student: {self.name}")

    def get_marks(self):
        print(self.marks)


    @staticmethod # This is Decorator
    def college():
        print("Welcome to College")



# creating object(instance)
s1 = Student("Karan", 97)
print(s1.name, s1.marks)
s1.welcome()
s1.get_marks()
s1.college()

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)

print(Student.college_name)







# Abstraction:- Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation:- Wrapping data and functions into a single unit(object).
# We make capsule of data and function in Encapsulation.

class Car1:

    def __init__(self):
        self.acc = False
        self.brk = True
        self.clutch = False
    
    def start_car(self):
        self.clutch = True
        self.acc = True
        print("Car Started...")

car1 = Car1()
car1.start_car()






# Practice:- Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    # Debit Balance Method
    def debit_balance(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print(f"Total Balance in Account {self.acc_no} is: {self.get_balance()}")
    
    # Credit Balance Method
    def credit_balance(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print(f"Total Balance in Account {self.acc_no} is: {self.get_balance()}")

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit_balance(1000)
acc1.credit_balance(500)



# del keyword :- Used to delete object properties or object itself.
# del s1.name       deleting object attributes
# del s1        deleting complete object




# Private(like) attributes & methods :- Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
# it is written in self.__acc_no   It is given by using two underscore before attributes
# You cannot private attributes & methods outside class
# Python have private, protected like other language private, protected.



# Inheritance:- When one class(child/derived) derives the properties & methods of another class(parent/base).

# Inheritance Types:-
"""
        - Single Inheritance:-  Single Parent Class and Single Child Class. Parent->Child
        - Multi-level Inheritance:-   Parent->Child->Child
        - Multiple Inhetitance
"""

class Car:
    
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car): # Single Inheritance

    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar): # Multi-Level Inheritance

    def __init__(self, type):
        self.type = type
    
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.brand)
print(car1.start())

car3 = Fortuner("Diesel")
print(car3.type)
car3.start()



# Multilevel Inheritance

class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B):
    varC = "Welcome to Class C"

c1 = C()

print(c1.varC, c1.varB, c1.varA)



# Super() method:- Is used to access methods of the parent class.

class Car2:
    
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar2(Car2): 

    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car10 = ToyotaCar2("Prius", "Electric")
print(car10.type)





