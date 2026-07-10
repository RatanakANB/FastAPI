# Lesson01 -Why OOP exists

# dog1_name = 'Milo'
# dog1_hunger = 7

# dog2_name = 'Luna'
# dog2_hunger = 3

def feed(name, hunger):
    hunger -= 2
    print(f'{name} has been fed. Hunger level is now {hunger}.')
    return hunger

def play(name, hunger):
    hunger += 1
    print(f'{name} has played. Hunger level is now {hunger}.')
    return hunger

# print("Before:")
# print(dog1_name, dog1_hunger)
# print(dog2_name, dog2_hunger)

# dog1_hunger = feed(dog1_name, dog1_hunger)
# dog1_hunger = play(dog1_name, dog1_hunger)

# dog2_hunger = feed(dog2_name, dog2_hunger)
# dog2_hunger = play(dog2_name, dog2_hunger)

# print("After:")
# print(dog1_name, dog1_hunger)
# print(dog2_name, dog2_hunger)

dog3_name = 'Max'
dog3_hunger = 10

print('Before:')
print(dog3_name, dog3_hunger)

dog3_hunger = feed(dog3_name, dog3_hunger)
dog3_hunger = play(dog3_name, dog3_hunger)

print('After:')
print(dog3_name, dog3_hunger)