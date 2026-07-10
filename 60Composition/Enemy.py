class Enemy:
    def __init__(self, name: str, health_points: int, attack_damage: int):
        self.name = name
        self.health_points = health_points
        self.attack_damage = attack_damage

    def attack(self):
        return self.attack_damage

    def take_damage(self, damage: int):
        self.health_points -= damage
        if self.health_points < 0:
            self.health_points = 0