
from Enemy import *

class Dragon(Enemy):
    def __init__(self, name, health, attack):
        super().__init__(type_of_enemy=name, health_points=health, attack_points=attack)