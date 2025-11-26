"""
Write a program that simulates rolling a six-sided dice and prints the result.
"""
# Roll the dice until the user wants to stop
import random

a =  random.randint(1,6)

while True:
    print(f"You rolled a {a}")
    again = input("Enter to roll a dice again. y/n : ")
    if again != 'y':
        break
    a = random.randint(1,6)



# Alternative solution:
while True:
    choice = input("Press Enter to roll the dice or type 'q' to quit: ")
    choice = choice.strip() # Remove any leading/trailing whitespace
    if choice.lower() == 'q':
        break
    elif choice == '':
        result = random.randint(1, 6)
        print(f"You rolled a {result}")
    else:
        print("Invalid input. Please try again.")
print("Thanks for playing!")


""" def roll_dice():
    return random.randint(1,6)

if __name__ == "__main__":
    result = roll_dice()
    print(f"You rolled a {result}")
"""