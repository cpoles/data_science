import re
from curses.ascii import isdigit, ispunct, isalpha

def split_phone(number):
    if len(number) == 11:
        ccode, area_code, ex_code, subs = number[0], number[1:4], number[4:7], number[7:]
        return ccode, area_code, ex_code, subs
    elif len(number) == 10:
        area_code, ex_code, subs = number[0:3], number[3:6], number[6:]
        return area_code, ex_code, subs

class PhoneNumber:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        cl_number = ''.join(re.findall('[^ .+\\-()]', number))
        print(cl_number)
        # no punctuation
        if any(ispunct(x) for x in cl_number):
            raise ValueError('punctuations not permitted')
        # no letters
        if any(isalpha(x) for x in cl_number):
            raise ValueError('letters not permitted')
        # less than 10 digits
        if len(cl_number) < 10:
            raise ValueError('incorrect number of digits')
        # more than 11 digits
        elif len(cl_number) > 11:
            raise ValueError('more than 11 digits')
        # 11 digits
        elif len(cl_number) == 11:
            ccode, area_code, ex_code, _ = split_phone(cl_number)
            # ccode must be 1
            if ccode != '1':
                raise ValueError("11 digits must start with 1")
            if area_code[0] == '0':
                raise ValueError("area code cannot start with zero")
            if area_code[0] == '1':
                raise ValueError('area code cannot start with one')
            if ex_code[0] == '0':
                raise ValueError("exchange code cannot start with zero")
            if ex_code[0] == '1':
                raise ValueError('exchange code cannot start with one')
            cl_number = cl_number[1:]
        elif len(cl_number) == 10:
            area_code, ex_code, _ = split_phone(cl_number)
            if area_code[0] == '0':
                raise ValueError("area code cannot start with zero")
            if area_code[0] == '1':
                raise ValueError('area code cannot start with one')
            if ex_code[0] == '0':
                raise ValueError("exchange code cannot start with zero")
            if ex_code[0] == '1':
                raise ValueError('exchange code cannot start with one')
        self._number = cl_number 

    @property
    def area_code(self):
        if len(self.number) == 11:
            _, area_code, _, _ = split_phone(self.number)
            return area_code
        elif len(self.number) == 10:
            area_code, _, _ = split_phone(self.number)
            return area_code 

    def pretty(self):
        if len(self.number) == 11:
            ccode, area_code, ex_code, subs = split_phone(self.number)
            return f'({area_code})-{ex_code}-{subs}' 
        elif len(self.number) == 10:
            area_code, ex_code, subs = split_phone(self.number)
            return f'({area_code})-{ex_code}-{subs}'
               

if __name__ == '__main__':
    number = PhoneNumber("12234567890")
    print(number.pretty())        

        