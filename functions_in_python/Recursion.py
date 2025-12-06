# Recursion is a process in which a function calls itself directly or indirectly.
# It is used to solve problems that can be broken down into smaller, similar subproblems.

# Factorial of a number without recursion
"""n = int(input("Enter a Number: "))
def Factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print(factorial)

Factorial(n)
"""


# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

a = int(input("Enter a Number: "))
factorial_of_a = factorial(a)
print(f"Factorial of {a} is: {factorial_of_a}")


