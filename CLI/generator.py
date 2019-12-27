import string  # Import the string Library
import random  # Import the random Library
from typing import Any, Union

alphabets: str = string.ascii_letters  # Initialize a string variable to store all letters from a-z lower and uppercase
digits: str = string.digits  # Initialize a string variable to store all the digits from 0-9
specialCharacters: str = string.punctuation  # Initialize a string variable to store all the special characters


def generatePassword(length):  # Create a function to generate a password of a required length
    password: str = ''  # Initialize a string variable password to store our generated password
    for i in range(0, length):  # A for loop to choose a random letter or number and add it to the password string
        typeChar = random.randint(0, 2)  # A variable that randomly receives a value 0 or 1 ,
        # '0' means the next character in the string will be an alphabet and 1 means the next character will be a
        # digit , if it is 2 then a special character
        if typeChar == 0:  # An if statement to check the value of the variable typeChar and append a
            # character to the string accordingly
            password += random.choice(alphabets)  # Chooses a random character from the alphabet string and appends
            # it the password string
        elif typeChar == 1:  # If the typeChar variable value is 1
            password += random.choice(digits)  # Choose a random digit from the digits string and append it to the
            # password variable
        elif typeChar == 2:  # If the typeChar variable value is 2 or 3
            password += random.choice(specialCharacters)  # Choose a random special character from the special
            # characters string and append it to the password variable

    return password  # On completion of the for loop and password has been generated , return the password string

# This line is only for testing the generator
print(generatePassword(20))  # Generate a password of length 20 characters and print it out on the console window
