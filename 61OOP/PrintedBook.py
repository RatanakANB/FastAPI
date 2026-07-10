from Book import Book


class PrintedBook(Book):
    def __init__(self, title: str, author: str, isbn: str, page_count: int):
        super().__init__(title, author, isbn)  # Inheritance: calling parent constructor
        self.__page_count = page_count  # Encapsulation: private attribute

    @property
    def page_count(self) -> int:
        return self.__page_count

    # Polymorphism: implementing abstract methods with specific behavior
    def get_details(self) -> str:
        return f"[Printed] '{self.title}' by {self.author} | Pages: {self.__page_count} | Available: {self.is_available}"

    def get_type(self) -> str:
        return "Printed Book"

    def estimate_reading_time(self) -> str:
        minutes = self.__page_count * 2  # Assume 2 minutes per page
        hours = minutes // 60
        remaining_mins = minutes % 60
        return f"Estimated reading time: {hours}h {remaining_mins}m"
