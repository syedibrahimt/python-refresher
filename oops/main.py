from oops.Dragon import Dragon
from oops.Enemy import Enemy
from oops.Zombie import Zombie

zombie = Zombie('ben10',200, 2)
dragon = Dragon('Dracarys', 1000, 10)

def battle(e: Enemy):
    e.walk()
    e.start_attack()

battle(zombie)
battle(dragon)

