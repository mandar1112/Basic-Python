
# Indentation(:) ==> it is used to define a block of code in Python.
# It indicates that the following indented lines belong to a specific control structure, such as an if statement, loop, or function definition.
# It helps in organizing the code and defining the scope of statements that should be executed together.
# It is essential for maintaining the structure and readability of the code.
# Indentation is typically done using spaces or tabs, and consistent indentation is crucial for Python's syntax. 4 spaces is the standard convention.


# if Block 

# Syntax:
# if condition:
     # code to be executed condition is 


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("You are not eligible to vote.")
    


# if else Block

num = int(input("Enter a number to check even or odd: "))

if num % 2 == 0:
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")



vote_age = int(input("Enter your age: "))
if vote_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("Thank you!")



# if elif else Block

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F - Fail")



# Nested if Block

marks = int(input("Enter The Marks: "))
if marks >= 50:
    if marks >= 90:
        print("Grade A")
    elif 80 <= marks < 90:
        print("Grade B")
    elif 70 <= marks < 80:
        print("Grade C")
    elif 60 <= marks < 70:
        print("Grade D")
    else:
        print("Grade E")
else: 
    print("Failed in Exam.")



# Ternary Operator is on ternary_operator.py file