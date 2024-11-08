import random
import string
import pyperclip

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Defining characters
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    # Combining characters for creating password
    all_characters = lower + upper + digits + special

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generating a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    #user input
    length = int(input("Enter Password length: ")) #length of password
    use_uppercase = input("Include uppercase ? (y/n): ").lower() == 'y' #uppercase or not
    use_digits = input("Include digits? (y/n): ").lower() == 'y' # should have digits?
    use_special = input("Include special characters? (y/n): ").lower() == 'y'  #include characters?

    #Generating password
    password = generate_password(length, use_uppercase, use_digits, use_special)

    # highlighting the generated password
    highlight_start = "\033[92m"  
    highlight_end = "\033[0m"     

    print(f"Generated Password: {highlight_start}{password}{highlight_end}")

    #copied the generated password 
    pyperclip.copy(password)
    print("Password copied to clipboard!")
