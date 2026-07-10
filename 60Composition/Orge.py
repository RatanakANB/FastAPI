from Enemy import Enemy

class Ogre(Enemy):
    def __init__(self, name: str, health_points: int, attack_damage: int, armor: int):
        super().__init__(name, health_points, attack_damage)
        self.armor = armor

    def take_damage(self, damage: int):
        # Damage is reduced by armor
        effective_damage = max(damage - self.armor, 0)
        super().take_damage(effective_damage)