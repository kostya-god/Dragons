# coding: utf-8
# license: GPLv3

from random import choice
from hero_classes import *

def generate_artifacts():
    enemy_list = [artifact_types[i] for i in range(len(artifact_types))]
    return enemy_list

class Artifacts():
    def __init__(self):
        self._cost = None
        self._name= None
        self._amount= None


class apple(Artifacts):
    _amount=0
    _name='apple'
    _cost=50

class marker(Artifacts):
    _amount = 0
    _name = 'marker'
    _cost=60


class shield(Artifacts):
    _amount = 0
    _name = 'shield'
    _cost =70


class rebirth(Artifacts):
    _amount = 0
    _name = 'rebirth'
    _cost =80


class wings(Artifacts):
    _amount = 0
    _name = 'wings'
    _cost =90


artifact_types=[apple, marker, shield, rebirth, wings]