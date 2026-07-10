from Book import Book


class Member:
    def __init__(self, name: str, member_id: str, max_books: int = 3):
        self.__name = name  # Encapsulation: private attribute
        self.__member_id = member_id
        self.__max_books = max_books
        self.__borrowed_books: list[Book] = []  # Composition: Member has Books

    @property
    def name(self) -> str:
        return self.__name

    @property
    def member_id(self) -> str:
        return self.__member_id

    @property
    def borrowed_count(self) -> int:
        return len(self.__borrowed_books)

    def borrow_book(self, book: Book) -> bool:
        if len(self.__borrowed_books) >= self.__max_books:
            print(f"{self.__name} cannot borrow more books. Limit: {self.__max_books}")
            return False
        if book.checkout():
            self.__borrowed_books.append(book)
            print(f"{self.__name} borrowed '{book.title}'")
            return True
        print(f"'{book.title}' is not available")
        return False

    def return_book(self, book: Book) -> bool:
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.__name} returned '{book.title}'")
            return True
        print(f"{self.__name} does not have '{book.title}'")
        return False

    def display_borrowed_books(self):
        print(f"\n--- {self.__name}'s Borrowed Books ---")
        if not self.__borrowed_books:
            print("No books borrowed.")
            return
        for book in self.__borrowed_books:
            print(f"  - {book.get_details()}")
        print("-----------------------------------\n")
