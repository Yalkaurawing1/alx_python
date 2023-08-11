#!/usr/bin/env python3

def validate_password(password):
   
    valid = True
   
    if len(password) < 8:
        valid = False
   
    if not any(char.isupper() for char in password):
        valid = False
    if not any(char.islower() for char in password):
        valid = False
    if not any(char.isdigit() for char in password):
        valid = False
   
    if not all(not char.isspace() for char in password):
        valid = False
    
    return valid

    
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
