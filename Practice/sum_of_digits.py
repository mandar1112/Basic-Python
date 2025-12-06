num = str(input("Enter a Number: "))
sum = 0
for i in range(len(num)):
    sum = int(num[i]) + sum
print(sum)

"""
# Another Way
num = input("Enter a Number: ")
sum = 0
for i in num:
    sum += int(i)
print(sum)
"""

num1 = input("Enter a Number: ")
sum_of_digit_of_number = 0
reversed_number = 0
while num > 0:
    digit = int(num1) % 10
    sum_of_digit_of_number = sum_of_digit_of_number + digit
    reversed_number = reversed_number * 10 + digit
    num1  = num1 // 10
print(sum_of_digit_of_number)
print(reversed_number)