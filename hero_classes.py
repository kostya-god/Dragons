# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.
"""

class Hero(Attacker):
    def __init__(self, name):
        self._health = 0
        self._attack = 0
        self._experience = 0
        self._name = name
        self._importance = 0
        self._money = 0
class Wizard(Hero):
        '''Возможно добавление скиллов'''
class Healer(Hero):
        '''Возможно добавление скиллов'''
class Jagernaut(Hero):
        '''Возможно добавление скиллов'''
class Imba(Hero):
        '''Возможно добавление скиллов'''



