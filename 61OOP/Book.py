from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title  # Encapsulation: private attribute
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    # Encapsulation: getter methods
    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def is_available(self) -> bool:
        return self.__is_available

    def checkout(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    # Abstraction: abstract method that must be implemented by subclasses
    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass
