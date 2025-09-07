from Enemy import *
class Zombie(Enemy):
    def __init__(self, type_of_enemy, health_points, attack_points):
        super().__init__(type_of_enemy= type_of_enemy, health_points= health_points,attack_points= attack_points)