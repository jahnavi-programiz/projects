import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    # Define the character sets to use in the password
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_digits, use_punctuation)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
