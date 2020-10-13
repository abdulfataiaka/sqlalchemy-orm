from db import Model
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer

class Author(Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(30))

    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f'Author({self.username})'
