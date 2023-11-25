"""
import random
import time

class Warrior:
    def __init__(self):
        self.health = 100

def attack(self, x):
    x.health -= 20


Pit = Warrior()
Jack = Warrior()

while (Jack.health > 0) and (Pit.health > 0):
    if random.randint(0, 1):
        Pit.attack(Jack)
        flag = 1
        print("Pit атаковал; Здоровье Jack: ", Jack.health, "\n")

    else:
        Jack.attack(Pit)
        flag = 0
        print("Jack атаковал; Здоровье Pit: ", Pit.health, "\n")
    time.sleep(1)

if flag:
    print("Победил Pit")
else:
    print("Победил Jack")

"""
import random

class Warrior():
    def __init__(self, hp, arm, stm, stat):
        self.hp = hp
        self.arm = arm
        self.stm = stm
        self.stat = stat

    def attack(self, unit):
        if unit.stat:
            if self.stm > 0:
                self.stm -= 10
                unit.hp -= random.randint(10, 30)
            else:
                unit.hp -= random.randint(0,10)
        else:
            if self.stm > 0:
                self.stm -= 10

    def protect(self, unit):
        if unit.stat:
            if self.arm > 0:
                self.arm -= random.randint(0, 10)
                if unit.stm > 0:
                    if self.arm > 0:
                        self.hp -= random.randint(0, 20)
                    else:
                        self.hp -= random.randint(10, 30)
                else:
                    self.hp -= random.randint(0, 10)

Jack = Warrior(100, 50, 50, 0)
Pit = Warrior(100, 50, 50, 0)

while (Jack.hp > 10) and (Pit.hp > 10):
    Pit.stat = random.randint(0, 1)
    Jack.stat = random.randint(0, 1)

    if Jack.stat:
        Jack.attack(Pit)
    else:
        Jack.protect(Pit)

    if Pit.stat:
        Pit.attack(Jack)
    else:
        Pit.protect(Jack)

print("Jack: ", Jack.hp, Jack.arm, Jack.stm, Jack.stat)
print("Pit: ", Pit.hp, Pit.arm, Pit.stm, Pit.stat, "\n")

if Jack.hp <= 10:
    print("Jack проиграл, pollice verso?")
if Pit.hp <= 10:
    print("Pit проиграл, pollice verso?")
