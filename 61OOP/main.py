from Library import Library
from Member import Member
from EBook import EBook
from PrintedBook import PrintedBook

# ============================================
# 61 - OOP: The 4 Pillars of Object-Oriented Programming
# Library Management System Example
# ============================================

# 1. ENCAPSULATION: Private attributes with getters
#    Book data is hidden, accessed only through properties

# 2. ABSTRACTION: Book is an abstract class
#    Users don't need to know how books work internally

# 3. INHERITANCE: EBook and PrintedBook inherit from Book
#    They share common behavior but have unique features

# 4. POLYMORPHISM: get_details() behaves differently
#    for EBook vs PrintedBook, but same interface

# Create library (Composition: Library contains Books)
library = Library("City Central Library")

# Create books (Inheritance: EBook and PrintedBook are Books)
ebook1 = EBook("Python Crash Course", "Eric Matthes", "978-1593279288", 5.2)
ebook2 = EBook("Clean Code", "Robert C. Martin", "978-0132350884", 3.8)
printed1 = PrintedBook("The Pragmatic Programmer", "Hunt & Thomas", "978-0135957059", 352)
printed2 = PrintedBook("Design Patterns", "Gang of Four", "978-0201633610", 395)
printed3 = PrintedBook("Atomic Habits", "James Clear", "978-0735211292", 320)

# Add books to library
library.add_book(ebook1)
library.add_book(ebook2)
library.add_book(printed1)
library.add_book(printed2)
library.add_book(printed3)

# Display all books (Polymorphism: get_details() called on different types)
library.display_all_books()

# Create members (Encapsulation: member data is private)
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002", max_books=2)

# Borrow books (Polymorphism: checkout works on any Book type)
member1.borrow_book(ebook1)
member1.borrow_book(printed1)
member1.borrow_book(printed2)

# Alice tries to exceed her limit
member1.borrow_book(printed3)

# Bob borrows books
member2.borrow_book(printed3)
member2.borrow_book(ebook2)

# Display borrowed books
member1.display_borrowed_books()
member2.display_borrowed_books()

# Search books (Polymorphism: search works with any Book subclass)
print("--- Search Results for 'Python' ---")
results = library.search_by_title("Python")
for book in results:
    print(f"  {book.get_details()}")

# Return a book
member1.return_book(printed1)

# Try to borrow an unavailable book
member2.borrow_book(ebook1)

# Show available books
print("\n--- Available Books ---")
for book in library.get_available_books():
    print(f"  {book.get_details()}")

# Demonstrate unique methods (Inheritance: specific behavior)
print(f"\n{ebook1.get_type()} specific: {ebook1.download()}")
print(f"{printed1.get_type()} specific: {printed1.estimate_reading_time()}")

# Final state
member1.display_borrowed_books()
library.display_all_books()
