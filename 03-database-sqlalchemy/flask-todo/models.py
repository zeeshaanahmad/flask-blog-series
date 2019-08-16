from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class TodoItem(Base):
    __tablename__='todoitem'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)