from models.book import BookModel
from sqlalchemy.orm import joinedload
from database import Book
from database import db_ops


class BookOps:
    def __init__(self) -> None:
        pass

    def get_all_books(self):
        session = db_ops.create_db_session()
        books = session.query(Book).options(joinedload(Book.author)).all()
        session.close()
        return books

    def get_book_by_id(self, id):
        session = db_ops.create_db_session()
        book = session.query(Book).options(joinedload(Book.author)).filter_by(id=id).first()
        session.close()
        return book

    def create_book(self, book: BookModel) -> None:
        res = 1
        try: 
            session = db_ops.create_db_session()
            book = Book(
                name=book.name,
                author_id=book.author_id,
                number_of_pages=book.number_of_pages,
            )
            session.add(book)
            session.commit()
            session.close()
        except Exception as e : 
            print(e)
            res = 0
        return {"result": res}


    def update_book(self, id, book: BookModel):
        session = db_ops.create_db_session()
        res = session.query(Book).filter_by(id=id).update(book.dict())
        session.commit()
        session.close()
        return {"result": res}

    def remove_book(self, id):
        session = db_ops.create_db_session()
        res = session.query(Book).filter_by(id=id).delete()
        session.commit()
        session.close()
        return {"result": res}


book_ops = BookOps()
