# Instance method => defined inside a class which is bound to or associated with the instance/object.


class Student:
    """
    This is a class Student to manage student info and activities.
    """

    def study(self, n_hours):  # This is instance method 
        print(f"The self is: {self}") 
        print(f"The Student studies for {n_hours} hours a day!")

    def sports(self, sport_name):
        print(f"The Student plays {sport_name}")
"""
student1 = Student()
print(student1) # Output:- <__main__.Student object at 0x000001AFC0E286E0>   This is memory address

print(f"The Object: {student1}")

# If i want to use study function
# student1.study() ==> this will give TypeError if any arg is not pass through instance method
# If you havent given any argument, then python will give it

def greet():
    print("Hello World!")
greet() # This give output

# By this we get to know that study is method 

student1.study()



When we call an instance method using the object/instance of the class, Python passes the object itself
as the first argument to that method.
The first argument is by standard is self
"""

student1 = Student()
print(f"The object: {student1}")
student1.study(3)
student1.sports("Football")
print("------------------------------------------------------------")
student2 = Student()
print(f"The object: {student2}")
student1.study(4)
student2.sports("Tennis")

"""
Output of student1 and student2

The object: <__main__.Student object at 0x000001AB55AB86E0>
The self is: <__main__.Student object at 0x000001AB55AB86E0>
The Student studies for 3 hours a day!
The Student plays Football

------------------------------------------------------------

The object: <__main__.Student object at 0x000001AB55ABC550>
The self is: <__main__.Student object at 0x000001AB55AB86E0>
The Student studies for 4 hours a day!
The Student plays Tennis

"""






