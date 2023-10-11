from pydantic import BaseModel, Field

class BookModel(BaseModel):
    name: str
    author_id: int
    number_of_pages: int