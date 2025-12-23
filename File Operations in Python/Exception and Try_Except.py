# Error Handling
# There are Two Types of Error in Python:
"""
Compile Time Error ==> Syntax error & Intendation Error
Example:-  age = 24  print(age  ==> Syntax Error
Example:-   age = 24
            if age >= 18:
            print("You are an Adult.")
            ==> This will give an Indentation Error.
"""
"""
Exceptions ==> Error Happen When we Execute The Program.
Like ZeroDivisionError: division by zero
"""

# How to Handle Exception ==> Using try-except block

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter Another Number: "))
result = num1/num2
print(result)
# ==> This will Exit the Code and Give Error.


try:
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter Another Number: "))
    result = num1/num2
    print(result)
except Exception as e:
    print("There is an Error: ",e)
except ZeroDivisionError:
    print("Error Division By Zero.")
except ValueError:
    print("Value Error: Input Should only be digits.")
