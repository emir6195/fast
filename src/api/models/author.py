from pydantic import BaseModel, Field
from models.book import BookModel
from typing import Optional, List


class AuthorModel(BaseModel):
    author: str
    books: Optional[List[BookModel]]

class AuthorUpdateModel(BaseModel):
    author: str