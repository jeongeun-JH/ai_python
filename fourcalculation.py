# coding: utf-8
"""A class for forur arithmetic calculations"""

class FourCalculation:
    """A class for forur arithmetic calculations"""

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if second == 0:
            raise ValueError('the number must NOT be zero')

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second
