# Initializer in Python
# __init__() method 
# Also called as Constructor
# It is an instance method 
# It is used to create and initialize the attributes during the object creation.

class Student:
    """
    This is a class Student to manage student info and activities
    """

    def __init__(self, name, roll, dept):
        print("Calling the initializer!")
        self.name = name # student1.name = "John"  same for student2
        self.roll = roll # student1.roll = 21  same for student2
        self.department = dept

    def study(self, n_hours):
        print(f"The student studies for {n_hours} hours a day!")
    
    def sports(self, sports_name):
        print(f"The student plays {sports_name}")


# This will automatically called the __init__ method and gives Output:- Calling the initializer!
# Methods like __init__ , etc are directly call when instance of the class is created.

student1 = Student("John", 21, "CS") 
student2 = Student("Carol", 22, "Arts")


print(student1.name, student1.roll, student1.department) # John 21 CS
print(student2.name, student2.roll, student2.department) # Carol 22 Arts


print(student1.__dict__) # {'name': 'John', 'roll': 21, 'Department': 'CS'}
print(student2.__dict__)


"""
Instance variable/attributes are different for different objects
"""



