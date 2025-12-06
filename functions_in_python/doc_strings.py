# Docstrings in Python
# What are Docstrings?
# Docstrings, or documentation strings, are a special type of comment used to describe the purpose of a function, class, or module in Python. They are enclosed in triple quotes (""" or ''') and are placed immediately after the definition of a function, class, or module.
# We can write what the function does, its parameters, return values, and any other relevant information in the docstring. This helps other developers (and ourselves) understand the code better.
# We can only write at start of the function.


def func():
    """
    This is a simple function that does nothing.

    Returns:
    None
    """

print(help(func))  # This will print the docstring of the function

def add(a,b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

