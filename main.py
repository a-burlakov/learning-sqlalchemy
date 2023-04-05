from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, relationship, sessionmaker

engine = create_engine("test", echo=True)
meta = MetaData()

authors = Table("Authors", meta, autoload=True)
books = Table("Books", meta, autoload=True)


class Book:
    def __init__(self, title, author_id, genre, price):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.price = price


class Author:
    def __init__(self, name):
        self.name = name


mapper(Book, books)
mapper(Author, authors)

new_book = Book("NewBook", 1, "New6", 2500)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(new_book)
session.commit()
