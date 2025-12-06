# Function as an Argument
# We can pass functions as arguments to other functions in Python.


def add(x):
    return x + 1
print(add(5))  # Output: 6
def square(x):
    return x ** 2
print(square(5))  # Output: 25

num = int(input("Enter a number: "))

res = square(add(num))
print("The result of squaring the incremented number is:", res)

def compute(add, square, num):
    result1 = add(num)
    result2 = square(result1)
    return result2
final_result = compute(add, square, num)
print("The final result is:", final_result) 
    