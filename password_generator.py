import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        print("  Please enter y or n.")

def get_length():
    while True:
        try:
            length = int(input("Password length (min 4): ").strip())
            if length >= 4:
                return length
            print("  Length must be at least 4.")
        except ValueError:
            print("  Please enter a valid number.")


# --- Main ---
print("=== Random Password Generator ===\n")

length       = get_length()
use_upper    = get_yes_no("Include uppercase letters? (y/n): ")
use_digits   = get_yes_no("Include digits?           (y/n): ")
use_symbols  = get_yes_no("Include symbols?          (y/n): ")

# Guard: at least one category must be active (lowercase is always included)
password = generate_password(length, use_upper, use_digits, use_symbols)

print(f"\nGenerated password: {password}")

