from Enemy import Enemy

class Zombie(Enemy):
    def __init__(self, name: str, health_points: int, attack_damage: int, decay_rate: int):
        super().__init__(name, health_points, attack_damage)
        self.decay_rate = decay_rate

    def decay(self):
        self.health_points -= self.decay_rate
        if self.health_points < 0:
            self.health_points = 0