import random
import string

def generate_password(length):
    # Characters to use in password
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print(" Password Generator ")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
