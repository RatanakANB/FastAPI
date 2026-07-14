"""Data models used by the lesson 02 book API."""

from typing import Optional
from pydantic import BaseModel, Field

class Book:
    """Represent a book stored in the in-memory collection."""

    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    
    def __init__(self, id, title, author, description, rating, published_date):
        """Initialize a book instance.

        Args:
            id: Unique identifier for the book.
            title: Book title.
            author: Author name.
            description: Short book description.
            rating: Book rating.
            published_date: date 2029
        """
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class bookRequest(BaseModel):
    """Validate incoming book payloads for create requests."""

    id : Optional[int] = Field(description='ID is not needed on create', default= None)
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description: str = Field(
        min_length=20,
        examples=[
            "I love this book because it explains FastAPI concepts clearly with practical and easy-to-follow examples for beginners."
        ,"idk"],
    )
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt= 1300, lt= 2026)
    
    model_config = {
        "json_schema_extra":{
            "example" : {
                'id': 99,
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2012
                
            }
        }
    }