# As a User need to enter a valid First Name - First name starts with Cap and has minimum 3 characters
# As a User need to enter a valid Last Name - Last name starts with Cap and has minimum 3 characters
# As a User need to enter a valid email - E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions
# As a User need to follow pre -defined Mobile Format - E.g. 91 9919819801 - Country code follow by space and 10 digit number
# As a User need to follow pre-defined Password rules. 
#   Rule 1 – minimum 8 Characters
#   Rule 2 – Should have at least 1 Upper Case
#   Rule 3 – Should have at least 1 numeric number 
#   Rule 4 – Should hava exaclty one special character 

import re
import logging

# Create logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# Create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create file handler and set level to warning
fh = logging.FileHandler('app.log')
fh.setLevel(logging.WARNING)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to handlers
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


Constraints = [
    {
        'title': 'First Name',
        'regex': r'^[A-Z][a-z]{2,}$',
        'message': 'First name starts with Cap and has minimum 3 characters: '
    },
    {
        'title': 'Last Name',
        'regex': r'^[A-Z][a-z]{2,}$',
        'message': 'Last name starts with Cap and has minimum 3 characters: '
    },
    {
        'title': 'Email',
        'regex': r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        'message': 'Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions: '
    },
    {
        'title': 'Phone',
        'regex': r'^91 [0-9]{10}$',
        'message': 'Country code follow by space and 10 digit number: '
    },
    {
        'title': 'Password',
        'regex': r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$&]).{8,}$',
        'message': 'Password must be minimum 8 characters and should have at least 1 Upper Case and 1 numeric number and exaclty one special character: '
    }
]

# Regex search utility
def check_validity(regex, value):
    """
    Description: This function checks if the given value matches the given regex.
    Arguments: {regex :string, value : string}
    Return: {matched :boolean}
    """
    return bool(re.search(regex, value))

def validate_first_name(user_input):
    """
    Description: Check if the given value matches the regex for the first name.
    Arguments: {user_input : string}
    Return: {matched :boolean}
    """
    regex = re.compile(Constraints[0]['regex'])  
    return check_validity(regex, user_input)

def validate_last_name(user_input):
    """
    Description: Check if the given value matches the regex for the last name.
    Arguments: {user_input : string}
    Return: {matched :boolean}
    """
    regex = re.compile(Constraints[1]['regex']) 
    return check_validity(regex, user_input)

def validate_email(user_input):
    """
    Description: Check if the given value matches the regex for the email.
    Arguments: {user_input : string}
    Return: {matched :boolean}
    """
    regex = re.compile(Constraints[2]['regex']) 
    return check_validity(regex, user_input)

def validate_phone(user_input):
    """
    Description: Check if the given value matches the regex for the phone number.
    Arguments: {user_input : string}
    Return: {matched :boolean}
    """
    regex = re.compile(Constraints[3]['regex'])
    return check_validity(regex, user_input)

def validate_password(user_input):
    """
    Description: Check if the given value matches the regex for the password and contains exactly one special character.
    Arguments: {user_input : string}
    Return: {matched :boolean}
    """
    regex = re.compile(Constraints[4]['regex'])  
    items = re.finditer(r'[@#$&]', user_input)
    return check_validity(regex, user_input) and len(list(items)) == 1


if __name__ == "__main__":
    while True:
        try:
            user_input = input(Constraints[0]['message'])
            if validate_first_name(user_input):
                logger.info("Validated First Name")
                break
            else:
                raise ValueError("Invalid First Name")
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            print(ve)

    while True:
        try:
            user_input = input(Constraints[1]['message'])
            if validate_last_name(user_input):
                logger.info("Validated Last Name")
                break
            else:
                raise ValueError("Invalid Last Name")
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            print(ve)

    while True:
        try:
            user_input = input(Constraints[2]['message'])
            if validate_email(user_input):
                logger.info("Validated Email")
                break
            else:
                raise ValueError("Invalid Email")
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            print(ve)

    while True:
        try:
            user_input = input(Constraints[3]['message'])
            if validate_phone(user_input):
                logger.info("Validated Phone Number")
                break
            else:
                raise ValueError("Invalid Phone Number")
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            print(ve)

    while True:
        try:
            user_input = input(Constraints[4]['message'])
            if validate_password(user_input):
                logger.info("Validated Password")
                break
            else:
                raise ValueError("Invalid Password")
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            print(ve)

