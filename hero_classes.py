# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.
"""

class Wizard(Attacker):
    def __init__(self, name):
        self._health = 75
        self._attack = 125
        self._experience = 0
        self._name = name
        self._importance = 1.5
        self._money = 100
class Healer(Attacker):
    def __init__(self, name):
        self._health = 50
        self._attack = 50
        self._experience = 0
        self._name = name
        self._importance = 0.5
        self._money = 100
class Jagernaut(Attacker):
    def __init__(self, name):
        self._health = 125
        self._attack = 60
        self._experience = 0
        self._name = name
        self._importance = 1.15
        self._money = 100
class Imba(Attacker):
    def __init__(self, name):
        self._health = 1000
        self._attack = 1000
        self._experience = 0
        self._name = name
        self._importance = 5
        self._money = 100


def attack(self, target):
    target._health -= self._attack
