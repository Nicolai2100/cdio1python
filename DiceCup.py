import random


class DiceCup:

    def __init__(self):
        self.sum = 0
        self.die1 = self.Die()
        self.die2 = self.Die()

    def roll_cup(self):
        self.die1.roll
        self.die2.roll
        self.sum = self.die1.face_value + self.die2.face_value
        return self.sum

    class Die:

        def __init__(self):
            self.face_value = 0

        def roll(self):
            self.face_value = random.randint(1, 6)
            return self.face_value


dc = DiceCup()
dc.roll_cup()
print(dc.sum)
print(dc.die2.face_value)
