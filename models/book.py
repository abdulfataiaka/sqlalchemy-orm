from db import Model
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey

class Book(Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    author_id = Column(ForeignKey('authors.id'))
    title = Column(String(80))

    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f'Book({self.title})'
