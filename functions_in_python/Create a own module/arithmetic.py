# A Simple Arithmetic Module

def add(num1,num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def squrt(number):
    return number ** 0.5

print(f"__name__ value in arithmetic.py => {__name__}") 

if __name__ == "__main__":
    a = 10
    b = 20
    print(a+b)

# This if __name__ == "__main__": helps to run the code in that when that file is run 