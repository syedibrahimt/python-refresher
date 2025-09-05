from Enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'Zombie'
enemy.health_points = 100
enemy.attack = 1

enemy.about_enemy()
enemy.talk()
enemy.walk()
enemy.start_attack()