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

Constrains = [
    {
        'title': 'First Name',
        'regex': '^[A-Z][a-z]{2,}$',
        'message': 'First name starts with Cap and has minimum 3 characters: '
    },
    {
        'title': 'Last Name',
        'regex': '^[A-Z][a-z]{2,}$',
        'message': 'Last name starts with Cap and has minimum 3 characters: '
    },
    {
        'title': 'Email',
        'regex': '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        'message': 'Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions: '
    },
    {
        'title': 'Phone',
        'regex': '^91 [0-9]{10}$',
        'message': 'Country code follow by space and 10 digit number: '
    },
    {
        'title': 'Password',
        'regex': '^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$&]).{8,}$',
        'message': 'Password must be minimum 8 characters and should have at least 1 Upper Case and 1 numeric number and exaclty one special character: '
    }
]

# Regex search utility
def check_validity(regex, value):
    if re.search(regex, value):
        return True
    else:
        return False

def validate_first_name(user_input):
    regex = re.compile(Constrains[0]['regex'])  
    return check_validity(regex, user_input)

def validate_last_name(user_input):
    regex = re.compile(Constrains[1]['regex']) 
    return check_validity(regex, user_input)

def validate_email(user_input):
    regex = re.compile(Constrains[2]['regex']) 
    return check_validity(regex, user_input)

def validate_phone(user_input):
    regex = re.compile(Constrains[3]['regex'])
    return check_validity(regex, user_input)

def validate_password(user_input):
    regex = re.compile(Constrains[4]['regex'])  
    if check_validity(regex, user_input):
        items = re.finditer(r'[@#$&]', user_input)
        return len(list(items)) == 1


if __name__ == "__main__":
    while not validate_first_name(input(Constrains[0]['message'])):
        pass
    while not validate_last_name(input(Constrains[1]['message'])):
        pass
    while not validate_email(input(Constrains[2]['message'])):
        pass
    while not validate_phone(input(Constrains[3]['message'])):
        pass
    while not validate_password(input(Constrains[4]['message'])):
        pass
