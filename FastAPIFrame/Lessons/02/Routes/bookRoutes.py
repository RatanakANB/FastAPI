"""HTTP routes for the lesson 02 book API."""

from fastapi import APIRouter

from Controller.bookController import bookreq, get_all_book
from Models.bookModel import bookRequest

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", description="hello world")
def read_all_books():
	"""Return the current list of books.

	Returns:
	    The shared in-memory book list.
	"""
	return get_all_book()


@router.post("/create-book")
def create_book(book_request: bookRequest):
	"""Create a new book from the request payload.

	Args:
	    book_request: Validated request body.

	Returns:
	    The created book object.
	"""
	return bookreq(book_request)
