import generator # Used to import the generator module which is in the same directory as this python file
from tkinter import Tk, Label, Button, Entry # Used to import the required modules from the tkinter library

app = Tk() # Used to create an application window


def generate(): # Create a function to be called when the button is clicked
    length = lenOfPassword.get() # Get the length of the password from the entry box and create a length variable to
    # store the value
    pswd = generator.generatePassword(int(length)) # Generate a password using the generator module and create a pswd
    # variable to store the value
    print(f"Your password: {pswd}") # Print the password on the console window


title = Label(app, text="Password Generator GUI") # Create the title label
lenLabel = Label(app, text="Enter Password Length") # Create the length label
lenOfPassword = Entry(app) # Create the length of password entry box to get input from the user
generateButton = Button(app, text="Generate Password", command=generate)  # Create the button to call the generate
# function when clicked

title.grid(row=0, column=0, columnspan=3) # Set the location of the title widget
lenLabel.grid(row=1, column=0, columnspan=2) # Set the location of the len label widget
lenOfPassword.grid(row=1, column=3) # Set the location of the lenOfPassword widget
generateButton.grid(row=2, column=0, columnspan=3) # Set the location of the generate button widget
