class Enemy:
    health_points: int
    attack: int
    type_of_enemy: str

    def about_enemy(self):
        print(f"The Enemy is of type {self.type_of_enemy} and he has {self.health_points} health points. He can do attack of {self.attack} point")

    def talk(self):
        print(f"Im your enemy {self.type_of_enemy}. I'm here to destroy you")

    def start_attack(self):
        print(f"Im attacking you with attack of {self.attack} point")

    def walk(self):
        print(f"Enemy {self.type_of_enemy} is walking around")