import sys
sys.path.insert(0, '../source')  
from main import * 
import pytest

Constrains_Cases = {
        'first_name' : [
            {'user_input' : 'Ab', 'expected' : False},
            {'user_input' : '123', 'expected' : False},
            {'user_input' : 'Abc', 'expected' : True},
            {'user_input' : 'Abc1', 'expected' : False},
            {'user_input' : 'Abc12', 'expected' : False},
            {'user_input' : 'Abc12345', 'expected' : False},
            {'user_input' : 'Rajesh', 'expected' : True},
            {'user_input' : 'Riya', 'expected' : True},
        ],
        'last_name' : [
            {'user_input' : 'Ab', 'expected' : False},
            {'user_input' : '123', 'expected' : False},
            {'user_input' : 'Abc', 'expected' : True},
            {'user_input' : 'Abc1', 'expected' : False},
            {'user_input' : 'Abc12', 'expected' : False},
            {'user_input' : 'Abc12345', 'expected' : False},
            {'user_input' : 'Singh', 'expected' : True},
            {'user_input' : 'Chatterjee', 'expected' : True},
        ],
        'emial' : [
            {"user_input": "abc", "expected" : False},
            {"user_input": "test.email@example.com", "expected": True},
            {"user_input": "user@domain.co", "expected": True},
            {"user_input": "first.last@sub_domain.com", "expected": True},
            {"user_input": "name+label@domain.info", "expected": False},
            {"user_input": "simple@example", "expected": False},
            {"user_input": "missingatsign.com", "expected": False},
            {"user_input": "username@.com", "expected": False},
            {"user_input": "username@com", "expected": False},
            {"user_input": "@missingusername.com", "expected": False},
            {"user_input": "user@domain..com", "expected": False}
        ],
        'phone' : [
            {'user_input' : '91 9919819801', 'expected' : True},
            {'user_input' : '91 991981980', 'expected' : False},
            {'user_input' : '9919819801', 'expected' : False},
            {'user_input' : '991981980', 'expected' : False},
            {'user_input' : '9919819801', 'expected' : False},
            {'user_input' : '991981980', 'expected' : False},   
        ],
        'password' : [
            {'user_input' : 'Abc12345', 'expected' : False},
            {'user_input' : 'Abc1234', 'expected' : False},
            {'user_input' : 'Abc123', 'expected' : False},
            {'user_input' : 'Abc12', 'expected' : False},
            {'user_input' : 'Abc1', 'expected' : False},
            {'user_input' : 'Abc', 'expected' : False},   
            {'user_input' : 'Abc12345@', 'expected' : True},
            {'user_input' : 'Abc12$34', 'expected' : True},
            {'user_input' : 'Abc1&23', 'expected' : False},
            {'user_input' : 'Abc12acg#', 'expected' : True},
        ]
}

def test_first_name():
    for i in Constrains_Cases['first_name']:
        assert validate_first_name(i['user_input']) == i['expected']

def test_last_name():
    for i in Constrains_Cases['last_name']:
        assert validate_last_name(i['user_input']) == i['expected']

def test_email():
    for i in Constrains_Cases['emial']:
        assert validate_email(i['user_input']) == i['expected']

def test_phone():
    for i in Constrains_Cases['phone']:
        assert validate_phone(i['user_input']) == i['expected']

def test_password():
    for i in Constrains_Cases['password']:
        assert validate_password(i['user_input']) == i['expected']  
