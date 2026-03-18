from random import randint
from random import choice
import string

"""class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

a = Die()
for i in range(10):
    a.roll_die()
print("Over!")

b = Die(10)
for i in range(10):
    b.roll_die()
print("Over!")

c = Die(20)
for i in range(10):
    c.roll_die()
print("Over!")"""

""" a = [randint(0, 10) for _ in range(10)]
b = [choice(string.ascii_letters) for _ in range(5)]
c = a + b
d = [choice(c) for _ in range(4)]
print(f"如果彩票上的数字或字母是{d}的话你就中大奖了！")

count = []
for i in range(100):
    n = 0
    while True:
        n += 1
        my_ticket = [choice(c) for _ in range(4)]
        if my_ticket == d:
            count.append(n)
            break
print(sum(count)/100) """
