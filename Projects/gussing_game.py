import random

def guessing_game():
    number_to_guess = random.randint(1,10)
    user_guess = None
    attempts = 0
    max_attempts = 5
    while user_guess != number_to_guess and attempts < max_attempts:
        user_guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("You guess is lower han the number.")
        elif user_guess > number_to_guess:
            print("Your guess is higher than the number.")
        else:
            print("Congratulations! You've guessed the number.")
            break
    
    if attempts == max_attempts and user_guess != number_to_guess:
        print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")

def main():
    guessing_game()

if __name__ == "__main__":
    main()