# check_protection.py

"""Formats user input for check protection printing"""

# import necessary libraries
from decimal import Decimal

def check_protection() -> str:
    '''Validates user input and returns formatted number'''
    try:
        value = input('Enter a value: ')
        value = Decimal(value)
    except:
        raise ValueError('Wrong value')
        
    return f'{value:*>10,.2f}'
    

print(check_protection())