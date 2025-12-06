num = input("Enter a number: ")
sum = 0
for i in range(len(num)):
    sum += int(num[i]) ** len(num)
if sum == int(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

