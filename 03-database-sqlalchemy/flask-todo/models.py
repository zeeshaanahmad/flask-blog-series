from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class TodoItem(Base):
    __tablename__='todoitem'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(), nullable=False)

engine = db.create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)