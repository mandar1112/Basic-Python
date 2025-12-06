def add(a,b):
    return a+b

# Positional Arguments:- Passing arguments in order of their position
result = add(10,20)


# Default Arguments:- Defining default values for parameters
def multiply(a, b=2):
    return a*b

mul = multiply(5)
print(mul)  # Output: 10

# The non-default argument cannot follow the default argument
# def divide(a=2, b):  # This will raise a SyntaxError

def addition(a,c, b=5):
    return a + b + c

addd = addition(10, 15)
print(addd)  # Output: 30


# Keyword Arguments:- Passing arguments by explicitly naming them. By using keyword arguments, the order of arguments can be changed.
# If keyword arguments are used, then the order of arguments does not matter.
def subtract(a, b):
    return a - b
sub = subtract(b=10, a=30)
print(sub)  # Output: 20

# Variable-length Arguments:- Allowing functions to accept an arbitrary number of arguments.
# Using *args for Non-keyword Variable-length Arguments
# *args allows you to pass a variable number of non-keyword arguments to a function.
# *args is a tuple of arguments passed to the function.
# *args must be the last parameter in the function definition.
# *args :- Variable length positional arguments (0 to n)
# *args :- collects extra positional arguments as a tuple




# Using **kwargs for Keyword Variable-length Arguments
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# **kwargs is a dictionary of arguments passed to the function.
# **kwargs must be the last parameter in the function definition.
# **kwargs:- can store tuples of key-value pairs
# **kwargs:- collects extra keyword arguments as a dictionary




def average(*args):
    return sum(args) / len(args)    
avg = average(10, 20, 30, 40)
print(avg)  # Output: 25.0

# Combining Different Types of Arguments
def complex_function(a, b=2, *args, **kwargs):
    result = a + b + sum(args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return result
complex_result = complex_function(10, 3, 4, 5, name="Test", age=25)
print(complex_result)  # Output: 22

def Student(sid,sname,*marks):
    print(sid)
    print(sname)
    print(marks)
    avg = sum(marks)/len(marks)
    return avg

std = Student(101,"Rock",35,86,678,876,908,345)
print(std)


