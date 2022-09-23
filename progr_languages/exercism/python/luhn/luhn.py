from unittest.signals import registerResult


class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):
        if len(self._card_num.strip()) <= 1:
            return False
        
        if not self.__validate_card_num(self._card_num):
            return False

        card_num = self._card_num.strip().split()
        # concatenate and reverse after split
        card_num = [char for group in card_num for char in group][::-1]
        # map str to int applying double and subtracting 9 when applicable
        final_card = []

        for idx, digit in enumerate(card_num):
            if self.__isOdd(idx):
                digit = self.__double(digit)
                final_card.append(digit)
            else:
                final_card.append(int(digit))
                
        # do the luhnCheck
        return self.__luhnCheck(final_card)
    
    def __validate_card_num(self, card_num):
        '''Checks if card_num string is valid'''
        card_num = self._card_num.strip().split()
        if all(map(lambda x: x.isdigit(), card_num)):
                return True
        return False


    def __isOdd(self, num):
        return True if num % 2 != 0 else False


    def __double(self, digit):
        '''Double str of digits and subtract 9 when the product is gt > 9'''
        digit = int(digit) * 2
        if digit > 9:
            digit -= 9
        return digit

    def __luhnCheck(self, digits):
        return sum(digits) % 10 == 0
