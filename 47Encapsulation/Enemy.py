# class Enemy:
    
#     type_of_enemy: str 
#     health_points: int = 100
#     attack_points: int = 1
    
#     def talk(self):
#         print(f'I am the {self.type_of_enemy}. Be prepared to fight! I have {self.health_points} health points and {self.attack_points} attack points.')
        
#     def attack(self):
#         print(f'The {self.type_of_enemy} moves closer to you.')
    
#     def attack2(self):
#         print(f'The {self.type_of_enemy} attacks you with {self.attack_points} attack points.')
        
   
class Enemy:
    def __init__(self, type_of_enemy: str , health_points: int = 100, attack_points: int = 1):
        self.__type_of_enemy: str = type_of_enemy
        self.health_points: int = health_points
        self.attack_points: int = attack_points

    def get_type_of_enemy(self):
        return self.type_of_enemy
    
    def set_type_of_enemy(self, type_of_enemy: str):
        self.type_of_enemy = type_of_enemy
        
    def talk(self):
        return f'''
      I am the Enemy,
      Enemy type: {self.type_of_enemy},
      '''