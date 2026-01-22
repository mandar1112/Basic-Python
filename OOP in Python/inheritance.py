# Inheritance
# The child/derived class takes properties from parent/base class.




# For example:

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat(self):
        print("Eating.")

class Teacher(Person):
    
    def teach(self):
        print(f"{self.name} is Teaching at the age of {self.age}.")
        self.eat()

a = Teacher("Mark", 25)
a.eat()
a.teach()

# Output:- 
#   Eating.
#   Mark is Teaching at the age of 25.
#   Eating.

# Try to use self.method() instead of directly calling the method.

# Note:-  If child class doesn't hve constructor(__init__), it will automatically call parent constructor in python.



# super() :- It is used to call methods or constructors of the parent class from a child class.
# it avoids writing the parent class name explicitly.
# Makes code cleaner, safer, and maintainable.


# Without super():-
#                   Parent __init__ will NOT run automatically
#                   Parent attributes won't be initialized.
#                   Causes runtime errors or missing data.


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating.")

class Teacher1(Person1):
    def __init__(self, name, age, subject):
        super().__init__(name, age) # Calling Parent Constructor
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject} at age {self.age}.")
        super().eat()     # Parent Method

t = Teacher1("Mark", 63, "Maths")
t.teach()

# Output:- Mark teaches Maths at age 63.
#          Mark is eating.





# Multilevel Inheritance :- A class inherits from a class, which itself inherits from another class.
# It forms a chain of inheritance.
# Grandparent -> Parent -> Child

# Child class gets all properties of parent & grandparents.
# Works top -> bottom.
# super() flows upward naturally.

class Person2:
    def speak(self):
        print("Person can speak.")

class Teacher2(Person2):
    def teach(self):
        print("Teacher can teach.")

class MathTeacher2(Teacher2):
    def subject(self):
        print("Math Teacher teaches Math")

m = MathTeacher2()
m.speak()
m.teach()
m.subject()

# Output:- 
#           Person can speak.
#           Teacher can teach.
#           Math Teacher teaches Math.





# Multiple Inhertitance:- A class inherits from more than one parent class.
# Child has multiple parents.
# Can reuse funtionality from different classes.
# Order matters


class Person3:
    def speak(self):
        print("Person can talk.")

class Employee:
    def work(self):
        print("Employee can work.")

class Teacher3(Person3, Employee):
    def teach(self):
        print("Teacher can teach.")

t3 = Teacher3()
t3.speak()
t3.work()
t3.teach()

# Output:- 
#           Person can speak.
#           Employee can work.
#           Teacher can teach.





# Diamond Problem
#      A
#    /   \
#   B     C
#   \    /
#     D


# Which parent's method should be called?
# Python Solution: MRO(Method Resolution Order)


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

print(D.mro())

d = D()
d.show()

# Output:- 
#           A
#           C
#           B
#           D





