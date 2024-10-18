#Genrating Random Values using random Module
import random
from random import randint


class Dice:
    def Roll(self):
            first = random.randint(1, 6)
            second = random.randint(1, 6)
            return first,second

dice1 = Dice()
print(dice1.Roll())

