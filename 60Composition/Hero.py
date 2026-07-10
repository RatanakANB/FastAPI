from Weapon import Weapon

class Hero:
    def __init__(self, name: str, health_points: int, attack_damage: int):
        self.name = name
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.weapon = None

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        damage = self.attack_damage
        if self.weapon:
            damage += self.weapon.attack_increase
        return damage

    def take_damage(self, damage: int):
        self.health_points -= damage
        if self.health_points < 0:
            self.health_points = 0