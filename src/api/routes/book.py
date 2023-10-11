from fastapi import APIRouter, Depends
from models.book import BookModel
from lib.book import book_ops
from lib.auth import JWTBearer

router = APIRouter()


@router.get("/",dependencies=[Depends(JWTBearer())], tags=["book"])
async def getAllBooks():
    books = book_ops.get_all_books()
    return books


@router.get("/{book_id}", dependencies=[Depends(JWTBearer())], tags=["book"])
async def getBookById(book_id):
    book = book_ops.get_book_by_id(book_id)
    return book


@router.post("/", dependencies=[Depends(JWTBearer())],  tags=["book"])
async def createBook(book: BookModel):
    _book = book_ops.create_book(book)
    return _book


@router.put("/{book_id}", dependencies=[Depends(JWTBearer())],  tags=["book"])
async def updateBook(book_id, book: BookModel):
    _book = book_ops.update_book(book_id, book)
    return _book


@router.delete("/{book_id}", dependencies=[Depends(JWTBearer())],  tags=["book"])
async def removeBookById(book_id):
    _book = book_ops.remove_book(book_id)
    return _book
