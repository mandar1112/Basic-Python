# Continue and break statements
# continue: skips the current iteration of a loop
# break: exits the loop entirely


# To print numbers from 0 to 59 that are not divisible by 2, 3, 5, or 7
# and stop the loop if the number reaches 59
b = []
for num in range(60):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        continue
    b.append(num)
    print(num)

    if num >=59:
        print("Reached 50, exiting loop.")
        break

print("Loop Exited")

for i in b:
    if i % 2 == 0:
        print(f"{i} is Even Number.")
    else:
        print(f"{i} is Odd Number. ")

