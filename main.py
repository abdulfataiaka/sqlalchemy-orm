from db import Session
from models import Author

session = Session()

author = Author(username='valerie', password='password')
session.add(author)
session.commit()

# book = Book(author_id=author.id, title='Example Title 3')
# session.add(book)
# session.commit()

# Queries

# result = session.query(Author).order_by(Author.id.desc()).slice(2,4).all()
# print(result)

# author = session.query(Author).first()

# print(author.books)

# Update & Delete

# Relationship

# Modularization

session.close()
