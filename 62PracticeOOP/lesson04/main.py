"""
```
Spot on! Existing objects (cookies already baked) keep their current structure and state, but any new objects created
  from the modified blueprint (future cookies) will have the new layout.
  ──────
  ### Continuity Checklist

  • Previous Lesson Mastery Gate: Passed (Lesson 03 — Class).
  • New Concept for this Turn: The concept of an Attribute (data/variables attached to a specific object).
  • Teaching Approach Adjustment: No adjustments; the blueprint-to-instance flow is clear.
  ──────
  ### Lesson 04 — Attribute

  #### Lesson Goal

  Understand that an Attribute is a variable bound to a specific object instance that holds that object's personal data.

  #### Directory Instructions

  Please create a new folder and files for this lesson:

  1. Create folder:  62PracticeOOP/lesson04/
  2. Create file:  62PracticeOOP/lesson04/Dog.py
  3. Create file:  62PracticeOOP/lesson04/main.py
  ──────
  #### Specification: Step 1

  Let's write our class blueprint and attach some data to an instance.

  • In  62PracticeOOP/lesson04/Dog.py :
      • Define an empty class named  Dog  (using  pass ).
  • In  62PracticeOOP/lesson04/main.py :
      • Import the  Dog  class.
      • Create a variable  dog1  and set it to a new instance of  Dog .
      • Use dot notation ( . ) to attach a  name  attribute to  dog1  and set it to the string  'Milo' .
      • Use dot notation to attach a  hunger  attribute to  dog1  and set it to the number  5 .
      • Print  dog1.name  and  dog1.hunger  on separate lines.


  Let me know once you have written this code!
```
"""
# from Dog import Dog

# Dog1 = Dog()
# Dog1.name = 'Milo'
# Dog1.hunger = 5
# print(f'Dog number 1 name: {Dog1.name}')
# print(f'Dog number 1 hunger: {Dog1.hunger}')

# dog2 = Dog()
# dog2.name = 'Luna'
# dog2.hunger = 3
# print(f'Dog number 2 name: {dog2.name}')
# print(f'Dog number 2 hunger: {dog2.hunger}')

from Book import Book

book1 = Book()
book1.title = 'OOP Basics'
book1.author = 'John Doe'

book2 = Book()
book2.title = 'Python Pro'
book2.pages = 300

print(f'{hasattr(book1, "pages")}')
print(f'{hasattr(book2, "pages")}')