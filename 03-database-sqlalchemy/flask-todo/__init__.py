from flask import Flask, render_template, request
from sqlalchemy import create_engine
from models import Base, TodoItem

# Setting up flask application
app = Flask(__name__)

# Creating engine by passing the path to our SQLite database
# to interact with it
engine = create_engine('sqlite:///todo.db')
Base.metadata.bind = engine

# Instatiating a session to interact with database 
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
def index():
    # Querying database for all the todo items
    todo_items = TodoItem.query().all()

    # redering index.html template with todo items retrieved 
    # from the databse
    return render_template("index.html", todo_items=todo_items)


@app.route("/add_todo", methods=['GET','POST'])
def insertTodo():
    try:
        todo_item_title = request.form['title']
        new_todo_item = TodoItem(title=todo_item_title)
        session.add(todo_item_title)

        return redirect(url_for('/'))

    except expression as identifier:
        abort(422)