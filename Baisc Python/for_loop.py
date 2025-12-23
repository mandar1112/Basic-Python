# For Loop

# Example
# To print a -- 10 times
a = "Hello World!"
sum = 1
for i in range(10):
    print(f"{sum}. {a}")
    sum += 1

"""Another way 
ls = ["Apples","Banana","Pear","Oranges"]
for i in range(len(ls)):
    b = ls[i]
    print(b)

    print(b)
"""

# Printing every char of the string
s1 = "Hello World!"
for char in s1:
    print(char)


# For loop in Dict

''' 
Employee = {'empid': 1001, 'name': 'John Gray', 'Department': 'HR'}
for i in Employee:
    print(i, Employee[i])
    print(f"{Employee.items()}, {Employee.keys()}, {Employee.values()}")

for i in Employee.items():
    print(i[0], i[1])
'''

# range() :- Built-in Function used to generate integers
# range(start, stop, step) :- stop is not included
# step is optional
# step default value is 1, start default value is 0, if only one argument is passed it is considered as stop value
# stop is mandatory, if range(5) => start=0, stop=5, step=1

# Generate numbers from 1 to 10
for i in range (1,11,1):
    print(i)


# Generate even numbers between 1 to 20
for i in range (2,21,2):
    print(i)


# Generate odd numbers between 1 to 20
for i in range (1,20,2):
    print(i)

# Print numbers from 10 to 1
for i in range (10,0,-1):
    print(i)
print("Happy New Year!")

# Print multiplication table of 5
num = 5
for i in range (1,20):
    print(f"{num} x {i} = {num*i}")

Profit = [9,11,10,12]
for i in range(len(Profit)):
    q = i + 1
    print(f"Quarter Profit: {q}, {Profit[i]}, {Profit.items()}")




scores = [65, 70, 89, 90, 34, 56, 78, 23, 88, 92, 100]
total = 0
length = len(scores)
for score in scores:
    total += score
print(f"Total Score: {total} \nPercentage: {(total/(length*100))*100}%")