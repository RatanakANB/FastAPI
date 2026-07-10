from Book import Book


class EBook(Book):
    def __init__(self, title: str, author: str, isbn: str, file_size_mb: float):
        super().__init__(title, author, isbn)  # Inheritance: calling parent constructor
        self.__file_size_mb = file_size_mb  # Encapsulation: private attribute

    @property
    def file_size_mb(self) -> float:
        return self.__file_size_mb

    # Polymorphism: implementing abstract methods with specific behavior
    def get_details(self) -> str:
        return f"[E-Book] '{self.title}' by {self.author} | Size: {self.__file_size_mb}MB | Available: {self.is_available}"

    def get_type(self) -> str:
        return "E-Book"

    def download(self) -> str:
        if self.is_available:
            return f"Downloading '{self.title}' ({self.__file_size_mb}MB)..."
        return f"'{self.title}' is currently checked out."
