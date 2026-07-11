    # Create two independent list objects
    dog1_hobbies = ['eating', 'sleeping']
    dog2_hobbies = ['eating', 'sleeping']

    # Check content equality (values) vs. object identity (memory location)
    print("Have same values:", dog1_hobbies == dog2_hobbies)  # True
    print("Are the same object:", dog1_hobbies is dog2_hobbies)  # False

    # Modify only one object using its built-in behavior (method)
    dog1_hobbies.append('playing')

    # Observe the results
    print("Dog 1 Hobbies:", dog1_hobbies)  # ['eating', 'sleeping', 'playing']
    print("Dog 2 Hobbies:", dog2_hobbies)  # ['eating', 'sleeping']