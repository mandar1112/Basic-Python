# Python Notes

# Literals ==> Are the fixed value written directly in the code, they represents the constant data that doesnt change during the program execution.
# x = 10
# y = 3.14
# z = 2j+3


# Variables ==> A variable is a name that give to a value in your program. It acts like a container that stores data, which you can use and change later.
# In above example x, y, z are variables.


# Keywords ==> They are special reserved words in Python that have a fixed meaning and purpose in the language. You cannot use them as variables. 
# Ex:- if, for, while, class, def, True, False, None, etc 
# import keywords
# keyword.kwlist()
# Output:- ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
#           'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


""" Data Types in Python """
"""
Text Type:	str
Numeric Types:	int, float, complex, double  
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


# Primitive Data Types ==>  They are basic built-in data types in a programming language. 
#           They store the simplest form of data and are building blocks for all other types.
#           They are basic units of data
# Ex:-  Integer(int)=> x = 10, Integers are whole numbers-numbers without decimal points. 
#       Floating Point(float)x = 3.14, Float represents numbers with decimal points
#       Boolena(bool)==> Represents True or False, Boolean represents truth value.
#       String(str)==> Represents text enclosed in quotes. Ex:- name = "Mandar"
# These are the four main primitive types in Python.


# Non-Primitive Data Types ==> They can store multiple value and are complex.
#           They are collection of data.
# Ex:-  list ==> Ordered, mutable collection. a = [1,2,3]
#       tuple ==> Ordered, immutable collection. a = (1,2,3)
#       dict ==> Key-value pairs. a = {"name": "Mandar", "age": 20}
#       set ==> Unorderd, unique items. a = {1,2,3}
#       bytes ==> Immutable sequence of bytes. b"Hello"
#       bytearray ==> Mutable sequence of bytes. bytearray(5)
#       range ==> Sequence of numbers. range(1,10)
#       frozenset ==> Immutable set. frozenset({1,2,3})


# Print ==> it can be written as:-
#           a = 10
#           print(a) 
#           print(100) 
#           print(a,100)
#           print(f"Value of a is {a}") ==> Output:- Value of a is 10
#           print("Value of a is:", a ,".") ==> Output:- Value of a is 10.
# If you print multiple values like print(10,20,30) ==> Output:- 10 20 30 ==> Their is by default space in it.
# Use of sep=" " in the print statement print(10,20,30 sep=",") ==> Output:- 10,20,30
# in sep=" " by default the space is their.

# f-string ==> It is used to format the string in a better way.
# Ex:- print(f"Day: {day} Month: {month} Year: {year}") ==> Output:- Day: 17 Month: 11 Year: 2025

# day = 17 month = 11, year = 2025 We want it like this 17/11/2025
# Then print(day,month,year sep="/") ==> Output:- 17/11/2025


# input() ==> This function is used to take input from the use
# Ex:- a = int(input("Enter a Number:")) ==> The Number will be only Integer
# if you write a = input("Enter a Number: ") ==> It will be by default string


# Comments ==> This is when we dont want to execute it, we just to want to write what it does.
# For single line comment we use:- #
# For multi line commnent we use:- """ """


s1 = "Hello World"
print(type(s1))

print(len(s1)) # To get to know the length of the string s1.

# What is Indexing?==> Accessing Every Individual Element within a sequence (such as a string, list or truple) by their position or index. 
# Ex:-  Python
#       012345  
#           Indexing can be negative if it done from right to left and it will start from -1.
#           in the Python if we use negative indexing then n will be -1,....., P will be -6.    

print(s1[3]) # To get to know the length of the s1
for i in range(len(s1)):
    print(s1[i])


# Type Conversion / Type Casting ==> Converting one data type into another if possible
# Type Conversion ==> Not all but we can convert most of data types into each other.
# a = 10
# type(a) ==> To get to know the data type of a 
# a = float(a) ==> Output:- 10.0
# bool(0) ==> Output:- False, if any value is their even space then it will True.
num1 = 100

num2 = float(num1)
print(num2)

num1 = float(num1)

lang = "Python"
version = 3.11

temp = lang + str(version)
print(temp)

# Arithmetic & Assignment Operators
# y,x -> Variable , 20 -> value this both are operands
# = + are operator

x = 10
y = x + 20

# Different Types of Operators
# 1. Arithmetic Operator ==> +,-,*,/
# for example
num3 = 10
num4 = 5
print(num3+num4)

print(f"Floor Division: {10//3}") #Floor Division

print(f"Modulus: {10%3}") # Modulus Operator give remainder

print(f"Exponent(power): {3**4}")# Exponent Operator use to get power of the given number or input


# 2. Assignment Operators

value = 100
add = num3 + num4
print(add)

# Component Assignment Operators
x = 10
x += 99
print(f"{x}")



# 3. Comparison Operators
# ==, !=, >, <, >=, <=

# 4. Logical Operators ==> and, or, not
# and ==> both conditon should be correct then only we get True
# or ==> either of any operant are true then it's true
# not ==> it returns true if oparant is false, it returns false if oparant is true

name = "Mark"
age = 25
print( name == "Mark" and age >= 18)
print( name == "Mark" and age <= 18)
print( name == "Mark" or age == 30)

# Precedence of Operators ==> priority in which operations are happens
# Associativity tells you the direction in which an expression is evaluated when two operators of the same precedence appear in an expression.
#           If two operators have equal precedence, Assocaiativity decides whether Python evaluates from Left to Right or Right to Left.


""" (Highest → Lowest)

Precedence	        Operators	                Associativity
1. Parentheses	    ()	                        N/A (forced first)
2. Exponent	        **	                        Right → Left
3. Unary	        + - ~	                    Right → Left
4. Multiplicative	* / // %	                Left → Right
5. Additive	        + -	                        Left → Right
6. Comparison	    < > == != <= >=	            Left → Right
7. Logical NOT	    not	                        Right → Left
8. Logical AND	    and	                        Left → Right
9. Logical OR	    or	                        Left → Right
10. Assignment	    = += -= *= /= //= %= **=	Right → Left"""

# Unary ==> It is a postive sign(+x), negative sign(-x), bitwise NOT sign(~x).

# Ternary Operator ==> In Python it is a one-line short form of an if-else statement, used to choose between two values.
""" It is also called the:
            Conditional Expression
            Inline if-else
            Ternary Operator """
# Syntax of Ternart Operator :- value_if_True if condition else value_if_false
# Ex:- 
""" x = 10 
result = "Positive" if x > 0 else "Negative"
print(result) """
# Output:- Positive


# Numeric Function ==> They are built-in Python Functions that are use to perform mathematical(numeric) operations on numbers. 
# They work on integers, floats, adn sometimes complex numbers. 
# They help you to perform calculations, rounding, converting numbers, finding absolute values, etc.

# max() Maximum Value ==> Returns a largest number. print(max(1,14,99,81)) ==> Output:- 99
# min() Minimum Value ==> Returns the smallest number. print(min(1,14,99,81)) ==> Output:- 1
# abs() Absolute Value ==> Returns the positive value of a number. print(abs(-2020))
# pow() Power Function ==> Raise a number to a power. pow(2,3) is equivalent to 2 ** 3 ==> Output:- 8
# round() Rounding ==> Rounds a number to the nearest integer or to given decimal places. round(3.7) ==> Output:- 4 or round(3.14159 , 2) ==> Output:- 3.14

# Advance Numeric Functions(Math module functions)
# To use this you have to "import math"

# math.sqrt() Square Root ==> math.sqrt(25) ==> Output:- 5
# math.ceil() Ceiling ==> Rounds up to nearest integer. ==> math.ceil(4.2) ==> Output:- 5
# math.floor() Floor ==> Rounds down to nearest integer. ==> math.floor(4.9) ==> Output:- 4
# Trigonometric Functions ==> this includes math.sin(x), math.tan(x), math.cos(x)
# Logarithmic Functions ==> This includes math.log(x), math.log10(x)

""" Table in short
    Function	                Purpose
    abs()	                    Absolute value
    pow(a, b)	                a raised to b
    round()	                    Round number
    min()	                    Smallest value
    max()	                    Largest value
    sum()	                    Add all values
    math.sqrt()	                Square root
    math.ceil()	                Round up
    math.floor()	            Round down
    math.sin() / math.cos()	    Trigonometry
    math.log()	                Logarithm
"""


# Slicing ==> It is a way to extract a portion of a sequence like a string, list, or tuple by specifying a start and end index.
# Syntax:- sequence[start:end:step]
text1 = "Hello, World!"
# print(text1[0:5]) # Output:- Hello
# print(text1[7:12]) # Output:- World
# print(text1[:5]) # Output:- Hello
# print(text1[7:]) # Output:- World!
# print(text1[::2]) # Output:- Hlo ol!
# print(text1[::-1]) # Output:- !dlroW ,olleH
# Reverse a String using Slicing
# reversed_text = text1[::-1]
# print(reversed_text) # Output:- !dlroW ,olleH




# Escape Sequences ==> They are special characters that are used to represent certain whitespace or non-printable characters within a string.
# They are used to format strings and control how text is displayed.
# Common Escape Sequences in Python:
# \n ==> New Line
# \t ==> Tab
# \\ ==> Backslash
# \' ==> Single Quote
# \" ==> Double Quote
# \r ==> Carriage Return 
# \b ==> Backspace
# \f ==> Form Feed
# \ooo ==> Octal Value
# \xhh ==> Hexadecimal Value
# Example of Escape Sequences
escaped_string = "Hello,\nWorld!\tThis is a tabbed line.\\"
print(escaped_string)



# Repeatition Operator ==> In Python, the repetition operator (*) is used to repeat a sequence (like a string, list, or tuple) multiple times.
# When you use the * operator with a sequence and an integer, it creates a new sequence that contains the original sequence repeated the specified number of times.
# Example of Repetition Operator
repeated_string = "Hello! " * 3
print(repeated_string)  # Output: Hello! Hello! Hello!



# Membership Operator ==> In Python, the membership operators are used to test whether a value or variable is present in a sequence (like a string, list, tuple, set, or dictionary).
# There are two membership operators:
# in ==> Returns True if the value is found in the sequence
# not in ==> Returns True if the value is not found in the sequence
# Example of Membership Operators
sample_list = [1, 2, 3, 4, 5]
print(3 in sample_list)      # Output: True
print(6 not in sample_list)  # Output: True


# Comparison Operators with Strings ==> In Python, you can use comparison operators to compare strings based on their lexicographical (dictionary) order.
# The comparison operators that can be used with strings are:
# == ==> Equal to
# != ==> Not equal to
# < ==> Less than
# > ==> Greater than
# <= ==> Less than or equal to
# >= ==> Greater than or equal to
# Example of Comparison Operators with Strings
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # Output: True (because "apple" comes before "banana" lexicographically)


# Removing Whitespace ==> In Python, you can remove whitespace from the beginning and end of a string using the strip() method.
# Example of Removing Whitespace
whitespace_string = "   Hello, World!   "
cleaned_string = whitespace_string.strip()
print(cleaned_string)  # Output: "Hello, World!"



# Replacement in Strings ==> In Python, you can replace occurrences of a substring within a string using the replace() method.
# Example of Replacement in Strings
original_string = "Hello, World! World!"
modified_string = original_string.replace("World", "Python")
print(modified_string)  # Output: "Hello, Python! Python!"



# String Methods ==> They are built-in functions that perform specific operations on strings.
# Some Common String Methods in Python:
# upper() ==> Converts all characters to uppercase.
# lower() ==> Converts all characters to lowercase.
# strip() ==> Removes leading and trailing whitespace.
# replace() ==> Replaces a specified substring with another substring.
# split() ==> Splits the string into a list of substrings based on a specified delimiter
# join() ==> Joins a list of strings into a single string with a specified delimiter.
# find() ==> Searches for a substring and returns its index or -1 if not found.
# title() ==> Converts the first character of each word to uppercase.
# capitalize() ==> Converts the first character of the string to uppercase and the rest to lowercase.


# Example of String Methods
sample_text = "  Hello, World!  "
print(sample_text.upper())        # Output: "  HELLO, WORLD!  "



# Counting Occurrences in Strings ==> In Python, you can count the occurrences of a substring within a string using the count() method.
# Example of Counting Occurrences in Strings
text = "banana"
count_a = text.count("a")
print(count_a)  # Output: 3

# Finding Substrings in Strings ==> In Python, you can find the index of the first occurrence of a substring within a string using the find() method.
# Example of Finding Substrings in Strings
text = "Hello, World!"
index_world = text.find("World")
print(index_world)  # Output: 7
# If the substring is not found, find() returns -1
index_python = text.find("Python")
print(index_python)  # Output: -1

s1 = "We are learning Python programming."
s2 = "e"
print(f"Occurrence of {s2} in s1 is: {s1.count(s2)}") # Output:- Occurrence of e in s1 is: 3


# Starting and Ending Check in Strings ==> In Python, you can check if a string starts or ends with a specific substring using the startswith() and endswith() methods.
# Example of Starting and Ending Check in Strings
text = "Hello, World!"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True
ends_with_world = text.endswith("World!")
print(ends_with_world)  # Output: False



