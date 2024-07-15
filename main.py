# As a User need to enter a valid First Name - First name starts with Cap and has minimum 3 characters

import re

def validate_first_name(first_name):
    regex = '^[A-Z][a-z]{2,}$'
    if re.search(regex, first_name):
        return True
    else:
        return False


first_name = input("Enter your first name: ")

if(validate_first_name(first_name)):
    print("Valid first name")
else:
    print("Invalid first name")
