# from Dog import Dog
# dog = Dog()

# dog2 = Dog()
# dog2.legs = 3
# dog2.ears = 2

# print(f'{dog.type} has {dog.legs} legs and {dog.ears} ears')
# print(f'{dog2.type} has {dog2.legs} legs and {dog2.ears} ears')

# ======= NOW THE ENEMY CLASS =======

# from Enemy import Enemy

# enemy = Enemy('zombie',123,3456754)

# enemy.__type_of_enemy = 'Orc'

# print(enemy.__type_of_enemy)


# enemy.walk_forward()

# enemy.attack()

# print(f'''
#       Enemy type: {enemy.type_of_enemy},
#       Has Health Points: {enemy.health_points},
#       And can do Attack Points: {enemy.attack_points}
#       ''')

# print(f'''
#       Enemy type: {zombie.type_of_enemy},
#       Has Health Points: {zombie.health_points},
#       And can do Attack Points: {zombie.attack_points}
#       ''')


class A:
      def action(self):
            print("Action in A")

class B(A):
      def action(self):
            print("Action in B")
            super().action()

class C(A):
      def action(self):
            print("Action in C")
            super().action()

class D(C, B):
      def action(self):
            print("Action in D")
            super().action()
            
d = D()
d.action()