import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    
    choice = int(input("Choose a difficulty level (1: Easy, 2: Medium, 3: Hard): "))
    match choice:
        case 1:
            attempts = 5
        case 2:
            attempts = 3
        case 3:
            attempts = 1
        case _:
            print("Invalid choice, defaulting to choose Easy Di attempts.")
            attempts = 5

    while attempts > 0:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess < number_to_guess:
            print("Your guess is lower than the number.")
        elif user_guess > number_to_guess:
            print("Your guess is higher than the number.")
        else:
            print("Congratulations! You've guessed the number.")
            return
        
        attempts -= 1
        print(f"You have {attempts} attempts left.\n")
    
    print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")

def main():
    guessing_game()

if __name__ == "__main__":
    main()
