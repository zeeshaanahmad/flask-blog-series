from flask import Flask, render_template, request, abort, url_for, redirect, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, TodoItem
import json

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
    todo_items = session.query(TodoItem).all()

    # redering index.html template with todo items retrieved 
    # from the databse
    return render_template("index.html", todo_items=[todo_item.serialize for todo_item in todo_items])


@app.route("/todo", methods=['GET','POST'])
def insertTodo():
    try:
        if request.method == 'GET':
            return render_template('new_todo.html')
        elif request.method == 'POST':
            todo_item_title = request.form['title']
            new_todo_item = TodoItem(title=todo_item_title)
            session.add(new_todo_item)
            session.commit()

            return redirect(url_for('index'))
    except:
        abort(422)

@app.route("/todo", methods=['PUT'])
def updateTodo():
    body = request.get_json()

    todo_id = body.get('id', None)

    todo_item = session.query(TodoItem).filter(TodoItem.id==todo_id).first()

    if todo_item is None:
        abort(404)

    todo_item.checked = body.get('checked')

    session.add(todo_item)
    session.commit()

    return jsonify({"success": True, "updated_todo": todo_id})


@app.route("/todo", methods=['DELETE'])
def deleteTodo():
    try:
        body = request.get_json()

        todo_id = body.get('id', None)

        todo_item = session.query(TodoItem).filter(TodoItem.id==todo_id).first()

        if todo_item is None:
            abort(404)
        
        session.delete(todo_item)
        session.commit()

        return jsonify({"success": True})
    except:
        abort(422)


@app.errorhandler(404)
def handle_404(error):
    return jsonify({"success": False, "message": "No Resource Found"})


@app.errorhandler(422)
def handle_422(error):
    return jsonify({"success": False, "message": "Unprocessable"})


@app.errorhandler(400)
def handle_400(error):
    return jsonify({"success": False, "message": "Bad request"})