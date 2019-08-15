# Flask To Do App - Part 2

As we learnt how to create a hello world applicaiton using Flask in my [previous post](../01-getting-started/readme.md), we'll go through basic structure of a web application built using Flask in this article.

## Basic Structure

We will create following structure in our flask-todo application that we started building in the previous article.

```
flask-app
.
├── __init__.py
├── static
│   ├── css
│   │   └── style.css
│   ├── img
│   │   └── cat.jpg
│   └── js
└── templates
    ├── index.html
    └── skeleton.html
```

As we have seen previously, the `__init__.py` module initializes our Flask application and acts as an entry point. We'll continue to add functionality to our to-do app and keep modifying this file. Later, I'll demonstrate how we can divide our application into separate modules.

### static

This directory will contain all the static content like css stylesheets, javascript files or images. This is why we will create separate sub-directories for each type of static content.

### static/css/style.css

It contains the styling for our application. We can define classes in this file and reuse them in our HTML templates. For our current sample, you can add following styles

```css
body {
    margin: 0;
    padding: 0;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #444;
  }

  header {
    background-color: #4c7d6c;
    height: 50px;
    width: 100%;
    opacity: .9;
    margin-bottom: 10px;
  }

  header h1.logo {
    font-size: 1.7em;
    color: #fff;
    text-transform: uppercase;
    float: left;
    margin-top: 10px;
  }

  header h1.logo:hover {
    color: #fff;
    text-decoration: none;
  }

  .container {
    width: 940px;
    margin: 0 auto;
  }

  div.jumbo {
    padding: 10px 0 30px 0;
    background-color: #4c7d6b47;
    margin-top: 25px;
    -webkit-border-radius: 25px;
       -moz-border-radius: 25px;
            border-radius: 25px;
  }

  h2 {
    font-size: 3em;
    margin-top: 40px;
    text-align: center;
    letter-spacing: -2px;
  }

  h3 {
    font-size: 1.5em;
    font-weight: 150;
    margin-top: 30px;
    text-align: center;
    letter-spacing: -1px;
    color: #a2a6b1;
  }
```

### static/js

Here we will add our javascript files. We do not need a javascript file for now so we can leave it empty.

### static/img

We will store images in this directory

## templates

This folder will contain HTML templates which we will use to render our application's user interface to client

### templates/skeleton.html

`skeleton.html` is an HTML template which will define basic layout of our application. 

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask Todo App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  </head>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">Flask Todo App</h1>
      </div>
    </header> 
     
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
     
  </body>
</html>
```

If you are familiar with HTML, you must be wondering what are `{{ url_for('static', filename='css/style.css') }}` or `{% block content %}` or `{% endblock %}`. This is because this file is a web template which can contain variables, conditional statements (`if`/`else` statements), control flows (`for` or `while` loops). In these template files we can perform logical operations and keep placeholders for content. Flask engine will understand these template files and render the required information accordingly. Flask uses [Jinja](https://jinja.palletsprojects.com/en/2.10.x/templates/) template library to render web templates.

In `skeleton.html` the statement `{% block content %}` is defining a block with the name `content` where we can insert some other HTML template on the runtime. It helps reducing the amount of repetitive HTML markup that we might have to keep adding in different HTML pages. For example, we want to keep our application header same throughout the application lifecycle, we do not want to keep repeating the HTML markup for header in all the page separately. Rather we can define an HTML template which only contains the header markup and keep reusing that in other HTML templates. It'll be clearer once you look at the `index.html` web template. `{% endblock %}` is simply defining the end of the `content` block. 

We can also call methods from our Python modules or other libraries by enclosing them within `{{ some_method() }}`. `{{ url_for('static', filename='css/style.css') }}` is one such example where we are calling `url_for` method for our `style.css` file which returns complete publicly accessible URL for that css file.

We'll be covering more of these web templates later. If you are interested in learning more about web templates, please visit the official documentation [here](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/).

### templates/index.html

```html
{% extends "skeleton.html" %}
{% block content %}
  <div class="jumbo">
    <h2>Welcome to the Flask To Do App<h2>
    <h3>Here you can create your To Do lists<h3>
  </div>
{% endblock %}
```

I hope the `content` block in `skeleton.html` makes more sense now. As you can see in the above snippet, we are reusing the `skeleton.html` and simply adding the markup for `content` block. This allows us to reuse application's layout defined in `skeleton.html` and define a new piece of content in a separate template. In future if we need to modify the `content` block or the application's layout, we'll only need to update the correspoding template. The changes will start reflecting without breaking any other templates.

### `__init__.py`

So, now we need to be able to see our html templates in action. We can do that by modifying the `__init__.py` and updating the `/` endpoint to return an HTML page.

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

Notice that we used `render_template()` method from `flask` and passed it the name of `index.html`. Flask by default looks for a folder named `templates` under our project root directory, processes it, builds the final HTML page and renders it to the client.

To learn more about `render_template()`, please visit this [resource](https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template).

## Conclusion

In this article we learnt about how to set up a simple application using web templates and render them. In the next article we'll learn how to integrate a database to our application and what technologies we can use.