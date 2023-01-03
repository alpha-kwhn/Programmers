import random


class Dice:

    def roll(self):
        self.num = random.randint(1, 6)
        return self.num


class FraudDice(Dice):
    def __init__(self, numbers):
        self.numbers = numbers

    def roll(self):
        while True:
            tmp = super().roll()
            if tmp == self.numbers:
                print(f"주사위 값 : {self.numbers} --> 원하는 값이 나왔습니다.")
                break
            else:
                print(f"주사위 값 : {tmp}")


e = FraudDice(3)
e.roll()




