"""
Class Methods => Methods defined inside the class that are bound to the class
To create a class method, we use a decorator -> @classmethod
It receives the class itself as the first argument -> cls

cls is a reference to the class
Conventionally:
        self -> object(instance)
        cls -> class
It can access class variables. But cannot directly access self.name or self.roll 


"""


class Welcome:
    
    @classmethod
    def greet(cls):  # We use cls as convention to capture the class name
        print(cls) # Output:- <class '__main__.Welcome'>
        print("Hello")

w1 = Welcome()
w1.greet()
print(Welcome) # Output:- <class '__main__.Welcome'>



class Student:
    """
    This is class Student
    """

    college_name = "ABC College"
    departments = ["Arts", "Commerce", "Science"]

    # __init__ is an constructor, automatically called when an object is created.
    def __init__(self, name, roll):
        print(f"Calling the initializer for self: {self}")
        self.name = name
        self.roll = roll
    
    def study(self, n_hours):
        print(self)
        print(f"The student studies for {n_hours} hours a day!")
    
    def sports(self, sports_name):
        print(f"The student plays {sports_name} in the college {self.college_name}")

    @classmethod
    def greet(cls):
        print(cls)
        print(f"Welcome to the {cls.college_name}")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are:")
        for department in cls.departments:
            print(department)

student1 = Student("John", 1001)
student1.study(3)
student1.greet() # Output:- <class '__main__.Student'>     Welcome to the ABC College
student1.sports("Football")
student1.get_departments()

