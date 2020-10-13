from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://127.0.0.1:5432/alchdb')

Model = declarative_base()

Session = sessionmaker(bind=engine)

def resetdb():
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)
