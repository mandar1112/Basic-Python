# Function in Python
# A function is a block of reusable code that performs a specific task.
# It helps to organize code, improve readability, and avoid repetition.
# Functions can built-in (like print(), len(), etc.) or user-defined.
# Defining a function

# Syntax:
"""def function_name(parameters):
    # Function body
    # Code to be executed
    return result  # Optional return statement
"""
# Example of a simple function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with multiple parameters
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# Function without parameters
def say_hello():
    return "Hello, World!"
print(say_hello())  # Output: Hello, World!

# Function with default parameter value
def power(base, exponent=2):
    return base ** exponent
print(power(3))        # Output: 9 (3^2)
print(power(2, 3))     # Output: 8 (2^3)



# Example:
def greets(name):
    return f"Hello, {name}!"

user_name = input("Enter Your Name: ")
print(greets(user_name))

def greetss():
    user_name = input("Enter Your Name: ")
    print(f"Hello, {user_name}!")

greetss()

# Function with multiple return values
def arithmetic(num1, num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    return add,sub,mul

val1,val2,val3 = arithmetic(10,20) # This is used to get all the three return value
print(val1,val2,val3)

# But if you want only mul value then

_,_,val3 = arithmetic(30,80) # _ this means that we doesnt care about the value
print(val3)




