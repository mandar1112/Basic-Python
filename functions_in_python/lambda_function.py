# Lambada Function
# A lambda function is a small anonymous function defined using the lambda keyword.
# It can take any number of arguments but can only have one expression.
# We can pass lambda functions as arguments to higher-order functions.
# We can write lambda functions in a single line.


# Syntax: lambda arguments: expression


# Example 1: A simple lambda function that adds 10 to the input number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

mul = lambda x, y: x * y
print(mul(2, 3))  # Output: 6