
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    author = Column(String())
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    author = relationship("Author", back_populates="books")
    author_id = Column(Integer, ForeignKey('authors.id'))
    number_of_pages = Column(Integer())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String())
    password = Column(String())
    role = Column(String())


class DbOps:
    def __init__(self) -> None:
        self.engine = create_engine(
            'sqlite:///challangeaccepted.db',
            echo=True
        )

    def initialize(self) -> None:
        # DB ops.
        Base.metadata.create_all(self.engine)

    def create_db_session(self):
        Session = sessionmaker(self.engine)
        return Session()


#  Initialize db.
db_ops = DbOps()
db_ops.initialize()
