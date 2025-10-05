import copy
from copy import deepcopy


class Character:
    def __init__(self, name, weapon, level, skill):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.skill = skill

    def clone(self):
        return deepcopy(self)
