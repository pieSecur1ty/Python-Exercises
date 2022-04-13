# import modules
import string
import random

# Function for generating password of particular size
def generate_password(size):
    all_strings = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(size):
        character = random.choice(all_strings)
        password = password + character
    return password


# user input and output
password_length = int(input("Enter the password length : "))
password = generate_password(password_length)
print(f"Password : {password}")
