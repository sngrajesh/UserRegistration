# As a User need to enter a valid First Name - First name starts with Cap and has minimum 3 characters
# As a User need to enter a valid Last Name - Last name starts with Cap and has minimum 3 characters
# As a User need to enter a valid email - E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions
# As a User need to follow pre -defined Mobile Format - E.g. 91 9919819801 - Country code follow by space and 10 digit number
# As a User need to follow pre-defined Password rules. 
# Rule 1 – minimum 8 Characters


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
        'regex': '^.{8,}$',
        'message': 'Password must be minimum 8 characters: '
    }
]

def check_validity(regex, value):
    if re.search(regex, value):
        return True
    else:
        return False

def validate():
    data = {}
    for constrain in Constrains:
        value = input(constrain['message'])
        while not check_validity(constrain['regex'], value):
            print(f'Invalid input for {constrain["title"]}. Please try again.')
            value = input(constrain['message'])
        data[constrain['title']] = value
        print(f'Valid {constrain["title"]}: {value}')
    return data

data = validate()
print(data)
