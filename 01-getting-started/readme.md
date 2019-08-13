
In this series, I'll help you get started with [Flask](https://palletsprojects.com/p/flask/). We are going to build a small to-do app with a restful back-end. We'll use React on the front-end.

# What is Flask

Flask is a Python web framework built on Web Server Gateway Interface [(WSGI)](https://wsgi.readthedocs.io/en/latest/what.html) [specifications](https://www.python.org/dev/peps/pep-3333/) aimed at building web applications quickly and easily.


# What do I need to know first

To follow along, you'll need to have basic understading of following:
* Python
* Javascript
* HTML
* CSS

# Environment Setup

## `virtualenv`

Since development environments differ and in order to stay on the same page while following along this series, it is a good idea to use `virtualenv` which creates an isolated Python development environment for us without messing up the existing set up.

### Install virtualenv

Using `pip`

```bash
$ sudo pip install virtualenv
```

Using `easy_install`

```bash
$ sudo easy_install virtualenv
```

If you are on Linux, you can use `apt-get` to install `vitualenv` on your system

```bash
$ apt-get install python-virtualenv
```

Here you can find installation instructions for `virtualenv` on [official documentation](https://virtualenv.pypa.io/en/latest/installation/)

As we have installed `virtualenv`, let's create a directory for our app called `flask-todo`

```bash
$ mkdir flask-todo
```

Go into the newly created directory

```
$ cd flask-todo
```

Now lets set up our virutal environment using `virtualenv`

```
$ virtualenv ENV
```

One more thing that we need to do is activate our isolated Python environment so that we start using it instead of any other version of Python on our system.

```
$ source ./ENV/bin/activate
```

### Flask

Once we have activated the virtual environment, we are ready to install Flask

```bash
$ pip install Flask
```

## Flask Hello World

Before we begin, let's create a basic Hello World application using Flask to see things in action.

Create a new python module named `__init__.py` inside `flask-todo` directory

```
$ touch __init__.py
```

At this point, I would suggest to use a code editor like [VS Code](https://code.visualstudio.com/download), [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3). I personally prefer VS Code.

You can open the `flask-todo` directory in your favorite code editor and start editing the `__init__.py` file

Let's first import `Flask`

```python
from Flask import flask
```

Initialize the Flask application

```python
app = Flask(__name__)
```

Add a default route 

```python
@app.route("/")
def index():
    return "Hello World!"
```

So, our `__init__.py` will look like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
```

In order to run our application, first lets set up some environment variables

```bash
$ cd ..
$ export FLASK_APP=flask-todo
$ export FLASK_ENV=development
```

Now run the application

```bash
$ flask run
```

It will start the Flask server hosting our app and we can access it at http://localhost:5000/ in our browser

The page should show `Hello World!` which means our basic `Flask` application has been set up properly and responding to HTTP requests.

# Conclusion

In this article we went through steps to create a virtual development environment using `virtualenv`, set up `Flask` and developed a Hello World application. In the next post we'll be setting up a directory sturcture for our `flask-todo` application, how to render HTML pages and static content.