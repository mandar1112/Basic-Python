# While:- A while loop repeatedly executes a block of code as long as a specified condition is true.
# While Vs For:- A for loop is used when the number of iterations is known beforehand, while a while loop is used when the number of iterations is not predetermined and depends on a condition.
# Example: Print "Hello World!" 10 times using a while loop.


i = 1
while i <= 10:
    print(f"{i}. Hello World!")
    i += 1
print("Finished!")


# Infinite While Loop

# Uncomment the following lines to see an infinite loop in action.

i = 1
while True:
    print(f"{i}. Good Morning.")
    i += 1
    if i > 50:
        break  # Added a break condition to prevent actual infinite loop during execution
print("Exited the infinite Loop.")

correct_password = "Python"


correct_password = "Python"
i = 0
while True:
    user_password = str(input("Enter Your Password: "))
    i += 1
    if user_password == correct_password:
        print("Correct Password.")
        break
    elif i > 3:
        print("Your account is baned for 30 min.")
        break
    else:
        print("Wrong Password. \nTry Again.")
print("Logged In....")


# Example: Print multiplication table of a number up to 20 using a while loop.
num = int(input("Enter a Number you want a Math Table: "))
i = 1
while i <= 20:
    print(f"{i}. {num} x {i} = {num*i}")
    i += 1
print(f"Multiplication Table of a Number {num} up to 20.")


