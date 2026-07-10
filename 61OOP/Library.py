from Book import Book


class Library:
    def __init__(self, name: str):
        self.__name = name  # Encapsulation: private attribute
        self.__books: list[Book] = []  # Composition: Library has Books

    @property
    def name(self) -> str:
        return self.__name

    def add_book(self, book: Book):
        self.__books.append(book)
        print(f"Added '{book.title}' to {self.__name}")

    def remove_book(self, isbn: str):
        for book in self.__books:
            if book.isbn == isbn:
                self.__books.remove(book)
                print(f"Removed '{book.title}' from {self.__name}")
                return
        print(f"Book with ISBN {isbn} not found")

    def search_by_title(self, title: str) -> list[Book]:
        # Polymorphism: works with any Book subclass
        return [book for book in self.__books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str) -> list[Book]:
        return [book for book in self.__books if author.lower() in book.author.lower()]

    def get_available_books(self) -> list[Book]:
        return [book for book in self.__books if book.is_available]

    def display_all_books(self):
        print(f"\n--- {self.__name} Catalog ---")
        if not self.__books:
            print("No books in catalog.")
            return
        # Polymorphism: get_details() behaves differently for each book type
        for book in self.__books:
            print(book.get_details())
        print("---------------------------\n")
