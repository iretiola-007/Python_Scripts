# import necessary modules
import random
import string

# define your function
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password 
    
# ask the user for desired length
length = user_input = input("Enter desired password length: ")

# then convert input to integer
try:
    length = int(user_input)
    print("Your new password is:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")


