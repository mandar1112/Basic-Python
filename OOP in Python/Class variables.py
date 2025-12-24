"""
Class Variables are defined at the class level.
Same copy of the class variables are shared among the objects.
"""

class Student:
    """
    This is class Student
    """

    college_name = "ABC College"
    departments = ["Arts", "Commerce", "Science"]


    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def study(self, n_hours):
        print(f"The student studies for {n_hours} hours a day!")
    
    def sports(self, sports_name):
        print(f"The student plays {sports_name}")


student1 = Student("John", 1001)
print(studen1.__dict__) # This will not show class variables. It will show instance variables
