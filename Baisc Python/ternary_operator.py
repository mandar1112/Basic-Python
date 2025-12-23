# Ternary Operator: A concise way to perform conditional assignments in Python.
# Syntax: value_if_true if condition else value_if_false
# In Ternary Operator, the condition is evaluated first. If it is True, the expression before 'if' is returned; otherwise, the expression after 'else' is returned.
# Means in one line we can write if-else condition.

# Example 1: Basic Usage
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")
# Output: Age: 20, Status: Adult

# Example 2: Using Ternary Operator in Function
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

num = 7
result = check_even_odd(num)
print(f"Number: {num}, Result: {result}")
# Output: Number: 7, Result: Odd