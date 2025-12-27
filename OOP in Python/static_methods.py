# Static Methods :- Methods defined inside a class which is neither bound to the object nor to the class.
# To Create a static method, we use staticmethod decorator.



class Student:
    """
    This is class Student
    """

    college_name = "ABC College"
    departments = ["Arts", "Commerce", "Science"]

    # __init__ is an constructor, automatically called when an object is created.
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def study(self, n_hours):
        print(f"The student studies for {n_hours} hours a day!")
    
    def sports(self, sports_name):
        print(f"The student plays {sports_name} in the college {self.college_name}")

    @staticmethod
    def greet():
        print(f"Welcome to the college")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are:")
        for department in cls.departments:
            print(department)


student1 = Student("John", 1001)
student1.greet()
student1.study(3)
student1.get_departments()
student1.greet()



 