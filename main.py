from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://127.0.0.1:5432/alchdb')

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(30))

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    title = Column(String(80))

# Creating Tables
def resetdb():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# resetdb()

# # Creating Session

Session = sessionmaker(bind=engine)
session = Session()

# author = Author(username='abdulfatai', password='password')
# session.add(author)

# book = Book(author_id=1, title='Example Title')
# session.add(book)

# session.commit()

# Queries

author = session.query(Author).first()
print(author.id)

# Update & Delete

# Relationship

# Modularization

session.close()
