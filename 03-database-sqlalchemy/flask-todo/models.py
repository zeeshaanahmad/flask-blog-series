from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class TodoItem(Base):
    __tablename__='todoitem'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    checked = Column(Boolean, nullable=False, default=False)

    @property
    def serialize(self):
        return {'id': self.id, 'title': self.title, 'checked': self.checked}

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)