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
        self.type_of_enemy: str = type_of_enemy
        self.health_points: int = health_points
        self.attack_points: int = attack_points

    def talk(self):
        return f'''
    I am the {self.type_of_enemy}. 
    Be prepared to fight! I have {self.health_points} 
    health points and {self.attack_points} attack points.
    '''