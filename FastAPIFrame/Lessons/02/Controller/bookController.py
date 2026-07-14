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


def get_book_by_id(book_id : int):
    for book in bookDatas:
        if book.id == book_id:
            return book
        
def get_book_by_rating(book_rating: int):
    books_to_return = []
    for book in bookDatas:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

def put_book_by_id(book_request):
    for i in range(len(bookDatas)):
        if bookDatas[i].id == book_request.id:
            bookDatas[i].id = book_request.id
            bookDatas[i].title = book_request.title
            bookDatas[i].author = book_request.author
            bookDatas[i].description = book_request.description
            bookDatas[i].rating = book_request.rating
            return bookDatas[i]
    
    return None


def delete_book_by_id(book_id):
    for i in range(len(bookDatas)):
        if bookDatas[i].id == book_id:
            bookDatas.pop(i)
            break
    #         return True

    # return False