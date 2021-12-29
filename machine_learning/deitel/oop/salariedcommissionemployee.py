# salariedcommissionemployee.py
'''SalariedCommissionEmployee derived from CommissionEmployee'''
from commissionemployee import ComissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(ComissionEmployee):
    '''An employee who gets paid a salary plus comission
        based on gross_sales.'''
    
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, salary):
        '''Set base salary or raise ValueError if invalid'''
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be gt zero')
        
        self._base_salary = salary
    
    def earnings(self):
        return super().earnings() + self.base_salary

    def __repr__(self) -> str:
        return (
            'Salaried' + super().__repr__() + 
            f'\nbase salary: {self.base_salary:.2f}'
        
        ) 
