from sqlalchemy import (
    create_engine,
    select,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
)

meta = MetaData()

authors = Table(
    "Authors",
    meta,
    Column("id_author", Integer, primary_key=True),
    Column("name", String(250), nullable=False),
)

books = Table(
    "Books",
    meta,
    Column("id_book", Integer, primary_key=True),
    Column("title", String(250), nullable=False),
    Column("author_id", Integer, ForeignKey("Author.id_author")),
    Column("genre", String(250)),
    Column("proce", Integer),
)

engine = create_engine("mysql+mysqlconnector://root:root@localhost/testdb", echo=True)
conn = engine.connect()

query = books.insert().values(title="test", price=999)
