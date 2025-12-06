# .py file is a module.
# Built-in Modules:- math, random, datetime, ....
# User defined Modules:- The python files created by user

# How to import a module in Python
# Syntax:- import module_name
# Syntax for  importing only few function/variables:-  from module_name import f1, f2, f3

# Syntax to create an alias for the module that is imported: import module_name as alias_name

import math
num = 100
output = math.sqrt(num)
print(output)
# Calculate square root of a number
# This is another way
from math import sqrt as sq

print(sq(9))

radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"Area of Circle of Radius {radius}: {area_of_circle}")


import datetime as dt

t = dt.time(8, 43, 51)
print(t)