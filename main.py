# As a User need to enter a valid First Name - First name starts with Cap and has minimum 3 characters
# As a User need to enter a valid Last Name - Last name starts with Cap and has minimum 3 characters

import re

def validate_string(user_input, regex):
    if re.search(regex, user_input):
        return True
    else:
        return False

regex = '^[A-Z][a-z]{2,}$'
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if validate_string(first_name, regex) and validate_string(last_name, regex):
    print("Valid input")
else:
    print("Invalid input")
