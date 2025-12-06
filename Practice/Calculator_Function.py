num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")
if operator == '+':
    result = num1 + num2
    print("The sum is:", result)
elif operator == '-':
    result = num1 - num2
    print("The difference is:", result)
elif operator == '*':
    result = num1 * num2
    print("The product is:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("The Division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    result = num1 % num2
    print("The Modulus is:", result)
else:
    print("Invalid operator")