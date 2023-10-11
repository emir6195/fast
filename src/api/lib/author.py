from models.author import AuthorModel
from sqlalchemy.orm import joinedload
from database import Author
from database import db_ops


class AuthorOps:
    def __init__(self) -> None:
        pass

    def get_all_authors(self):
        session = db_ops.create_db_session()
        authors = session.query(Author).options(joinedload(Author.books)).all()
        session.close()
        return authors
    
    def get_all_authors_without_join(self):
        session = db_ops.create_db_session()
        authors = session.query(Author).all()
        session.close()
        return authors

    def get_author_by_id(self, id):
        session = db_ops.create_db_session()
        author = session.query(Author).filter_by(
            id=id).options(joinedload(Author.books)).first()
        session.close()
        return author

    def create_author(self, author: AuthorModel) -> None:
        res = 1
        try:
            session = db_ops.create_db_session()
            author = Author(
                author=author.author,
                books=author.books
            )
            session.add(author)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
            res = 0
        return {"result": res}

    def update_author(self, id,  author: AuthorModel):
        session = db_ops.create_db_session()
        res = session.query(Author).filter_by(id=id).update(author.dict())
        session.commit()
        session.close()
        return {"result": res}

    def remove_author(self, id):
        session = db_ops.create_db_session()
        res = session.query(Author).filter_by(id=id).delete()
        session.commit()
        session.close()
        return {"result": res}


author_ops = AuthorOps()
