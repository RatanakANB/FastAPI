"""HTTP routes for the lesson 02 book API."""

from fastapi import APIRouter, HTTPException

from Controller.bookController import put_book_by_id, \
                                    get_book_by_rating, \
                                    bookreq, \
                                    get_all_book, \
                                    get_book_by_id, \
                                    delete_book_by_id
from Models.bookModel import bookRequest

routerBook = APIRouter(prefix="/books", tags=["books"])

@routerBook.get("/", description="hello world")
async def read_all_books():
	"""Return the current list of books.

	Returns:
	    The shared in-memory book list.
	"""
	return get_all_book()

@routerBook.post("/create-book")
async def create_book(book_request: bookRequest):
	"""Create a new book from the request payload.

	Args:
	    book_request: Validated request body.

	Returns:
	    The created book object.
	"""
	created_book = bookreq(book_request)
	return created_book

@routerBook.get("/{book_id}")
async def get_book_id(book_id: int):
	book = get_book_by_id(book_id)
	if book is None:
		raise HTTPException(status_code=404, detail="Book not found")
	return book

@routerBook.get("/rating/{book_rating}")
async def get_book_rating(book_rating: int):
	book = get_book_by_rating(book_rating)
	if not book:
		raise HTTPException(status_code=404, detail="No books found for this rating")
	return book

@routerBook.put("/update_book")
async def put_book_id(book_request: bookRequest):
	book = put_book_by_id(book_request)
	if book is None:
		raise HTTPException(status_code=404, detail="Book not found")
	return book

@routerBook.delete("/{book_id}")
async def delete_book(book_id: int):
	delete_book_by_id(book_id)
	# if not deleted:
	# 	raise HTTPException(status_code=404, detail="Book not found")