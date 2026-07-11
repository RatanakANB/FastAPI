# ### Continuity Checklist

#   • Previous Lesson Mastery Gate: Passed (Lesson 02 — Object).
#   • New Concept for this Turn: The concept of a "Class" as a blueprint/template to construct custom objects.
#   • Teaching Approach Adjustment: No adjustments needed; the cardboard box and sticky note analogy was highly effective,
#   so we will extend it to explain classes.
#   ──────
#   ### Lesson 03 — Class

#   #### Lesson Goal

#   Understand that a Class is a custom blueprint or template used to construct individual objects (instances) with a
#   shared type.

#   #### Illustrative Example (New Syntax)

#   Since defining a class is brand-new syntax, here is a short example of how to define a custom blueprint and use it.

#   If we wanted to make a blueprint for a Car:

#   Inside  Car.py :

#     class Car:
#         pass  # 'pass' is just a placeholder that does nothing

#   Inside  main.py :

#     # Import the Car class from the Car.py file
#     from Car import Car

#     # Construct a new Car object (instance) using the blueprint
#     my_car = Car()
#     ──────
#   #### Directory Instructions

#   Please create the following folder and files:

#   1. Create a new folder:  62PracticeOOP/lesson03/
#   2. Create a file inside it:  62PracticeOOP/lesson03/Dog.py
#   3. Create another file inside it:  62PracticeOOP/lesson03/main.py
#   ──────
#   #### Specification: Step 1

#   Now write the code for the first chunk:

#   • In  62PracticeOOP/lesson03/Dog.py : Define a custom class named  Dog . Use  pass  as the body of the class so it
#   remains empty for now.

#   Let me know once you have created the folder/files and written this class definition!

from Dog import Dog
from Cat import Cat

my_dog = Dog()
my_cat = Cat()

dog1 = Dog()
dog2 = Dog()


print(type(dog1))
print(dog1 is dog2)
print(type(Dog))


print(type(my_dog) == type(my_cat))
print(type(my_dog) == Dog)
print(Dog)










