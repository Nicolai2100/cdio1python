import random

class DiceCup:
    sum = 0

    def __init__(self):
        pass

    def roll(self):
        self.sum = random.randint(1, 6)
        return sum
