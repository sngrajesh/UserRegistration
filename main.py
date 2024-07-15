# As a User need to enter a valid First Name - First name starts with Cap and has minimum 3 characters
# As a User need to enter a valid Last Name - Last name starts with Cap and has minimum 3 characters
# As a User need to enter a valid email - E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions
# As a User need to follow pre -defined Mobile Format - E.g. 91 9919819801 - Country code follow by space and 10 digit number

import re

def validate_string(user_input, regex):
    if re.search(regex, user_input):
        return True
    else:
        return False

name_regex = '^[A-Z][a-z]{2,}$'
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = input("Enter your email: ")

phone_regex = '^[0-9]{2} [0-9]{10}$'
phone = input("Enter your phone number: ")

if validate_string(phone, phone_regex):
    print("Valid input")
else:
    print("Invalid input")

if validate_string(first_name, name_regex) and validate_string(last_name,name_regex) and validate_string(email, email_regex):
    print("Valid input")
else:
    print("Invalid input")
