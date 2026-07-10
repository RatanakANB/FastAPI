# from Dog import Dog
# dog = Dog()

# dog2 = Dog()
# dog2.legs = 3
# dog2.ears = 2

# print(f'{dog.type} has {dog.legs} legs and {dog.ears} ears')
# print(f'{dog2.type} has {dog2.legs} legs and {dog2.ears} ears')

# ======= NOW THE ENEMY CLASS =======

from Enemy import Enemy

enemy = Enemy('Orc',123,3456754)
zombie = Enemy('Zombie',432,"23456765432")

print(enemy.talk())
# print(enemy.attack())

print(zombie.talk())
# print(zombie.attack())

# enemy.talk()
# enemy.attack()

# zombie.talk()
# # zombie.attack()

print(f'''
      Enemy type: {enemy.type_of_enemy},
      Has Health Points: {enemy.health_points},
      And can do Attack Points: {enemy.attack_points}
      ''')

print(f'''
      Enemy type: {zombie.type_of_enemy},
      Has Health Points: {zombie.health_points},
      And can do Attack Points: {zombie.attack_points}
      ''')

