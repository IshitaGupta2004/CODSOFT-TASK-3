import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Creating empty character set
    characters = ''
    
    # Adding character sets based on user preferences
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensuring that at least one character set is selected
    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password using the specified length and character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#for adding output design
def print_in_box(password):
    box_size = len(password)+6
    print("-" * box_size)
    print(f"|  {password}  |")
    print("-" * box_size)

def main():
    print("Welcome to the Your Password Generator!")

    # Get user input for the password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8): "))
            if length < 8:
                print("Please enter a length of at least 8.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (y if yes /n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y if yes /n): ").lower() == 'y'
    use_digits = input("Include digits? (y if yes /n): ").lower() == 'y'
    use_special = input("Include special characters? (y if yes /n): ").lower() == 'y'

    # Generating the password
    try:
        generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        # Display the generated password
        print("Suggested Password:")
        print_in_box(generated_password)
        print("thank you for choosing us")    
    except ValueError as e:
        print(e)
        

# Run the main function
if __name__ == "__main__":
    main()
