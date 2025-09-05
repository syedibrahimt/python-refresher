class Enemy:

    def __init__(self, type_of_enemy, health_points = 100, attack_points = 1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_points = attack_points

    def about_enemy(self):
        print(f"The Enemy is of type {self.type_of_enemy} and he has {self.health_points} health points. He can do attack of {self.attack_points} point")

    def talk(self):
        print(f"Im your enemy {self.type_of_enemy}. I'm here to destroy you")

    def start_attack(self):
        print(f"Im attacking you with attack of {self.attack_points} point")

    def walk(self):
        print(f"Enemy {self.type_of_enemy} is walking around")