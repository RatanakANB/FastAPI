# dog1_hobbies = ['eating', 'sleeping']
# dog2_hobbies = ['eating', 'sleeping']

# print(dog1_hobbies == dog2_hobbies)
# print(dog1_hobbies is dog2_hobbies)

# dog1_hobbies.append('playing')
# print(dog1_hobbies)
# print(dog2_hobbies)

# # ===== Experimental =====
# dog2_hobbies = dog1_hobbies
# print(dog1_hobbies is dog2_hobbies)

# ===========
### Challenge (Mini Challenge)

dog_a = {
    "name": "Rex",
    "energy": 100,
}

dog_b = dog_a

dog_c = {
    "name": "Rex",
    "energy": 100,
}

dog_b["energy"] = 80

print(dog_a["energy"]) 
print(dog_b["energy"])
print(dog_c["energy"])