import string
import random

class Robot:
    def __init__(self):
        self.name = self._create_name()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self._create_name()

    def _create_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers

    def reset(self):
        random.seed(random.randint(0, 100))
        self.name = self._create_name()
