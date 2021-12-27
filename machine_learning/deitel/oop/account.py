# account.py
'''Account class definition'''
from decimal import Decimal

class Account:
    '''Account class for maintaining a bank account balance'''
    def __init__(self, name, balance) -> None:
        '''Initialize aan Account object'''
        
        # if balance is less than 0.00, raise na exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        '''Deposit money to the acccount'''

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount

    def withdrawal(self, amount):
        '''Withdrawal money from the account'''

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        
        # if the amount is greater than the balance, raise an exception
        elif amount > self.balance:
            raise ValueError('amount must be <= to account balance')
        
        self.balance -= amount