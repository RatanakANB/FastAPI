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
    
    def __init__(self, id, author, title, description, rating):
        """Initialize a book instance.

        Args:
            id: Unique identifier for the book.
            author: Author name.
            title: Book title.
            description: Short book description.
            rating: Book rating.
        """
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

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
    
    model_config = {
        "json_schema_extra":{
            "example" : {
                'id': 99,
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description of a book',
                'rating': 5
            }
        }
    }