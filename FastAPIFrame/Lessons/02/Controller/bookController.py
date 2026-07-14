"""Controller functions for the lesson 02 book API."""

from Data.bookData import bookDatas
from Models.bookModel import Book


def get_all_book():
    """Return all books currently stored in memory.

    Returns:
        The list of book objects in the shared collection.
    """
    return bookDatas


def bookreq(book_request):
    """Create a new book and add it to the shared collection.

    Args:
        book_request: Validated request payload from the route layer.

    Returns:
        The newly created book object.
    """
    new_book = Book(**book_request.model_dump())
    new_book = find_book_id(new_book)
    bookDatas.append(new_book)
    return new_book


def find_book_id(book: Book):
    """Assign the next sequential ID to a new book.

    Args:
        book: Newly created book object.

    Returns:
        The same book object with an assigned ID.
    """
    book.id = 1 if len(bookDatas) == 0 else bookDatas[-1].id + 1
    return book
