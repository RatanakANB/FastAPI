from Hero import Hero
from Weapon import Weapon
from Enemy import Enemy
from Zombie import Zombie
from Orge import Ogre

# Create a hero
hero = Hero("Archer", 100, 10)
# Create a weapon
sword = Weapon("Sword", 15)
hero.equip_weapon(sword)

# Create enemies
zombie = Zombie("Zombie", 50, 5, decay_rate=2)
ogre = Ogre("Ogre", 150, 20, armor=5)

# Hero attacks zombie
damage = hero.attack()
zombie.take_damage(damage)
print(f"Zombie health after attack: {zombie.health_points}")

# Zombie attacks hero
hero.take_damage(zombie.attack())

# Hero attacks ogre
damage = hero.attack()
ogre.take_damage(damage)
print(f"Ogre health after attack: {ogre.health_points}")

# Ogre attacks hero
hero.take_damage(ogre.attack())

print(f"Hero health: {hero.health_points}")

def battle(enemy1: Enemy, enemy2: Enemy):
    # Example attack and dialogue
    print(f"{enemy1.name} attacks!")
    enemy1_damage = enemy1.attack()
    enemy2.take_damage(enemy1_damage)
    print(f"{enemy2.name} takes {enemy1_damage} damage! Remaining health: {enemy2.health_points}")

    print(f"{enemy2.name} attacks!")
    enemy2_damage = enemy2.attack()
    enemy1.take_damage(enemy2_damage)
    print(f"{enemy1.name} takes {enemy2_damage} damage! Remaining health: {enemy1.health_points}")

# Create instances
zombie = Zombie("Zombie", 50, 5, decay_rate=2)
ogre = Ogre("Ogre", 150, 20, armor=5)

# Start a battle between a zombie and an ogre
battle(zombie, ogre)