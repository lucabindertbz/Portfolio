# This is a Flask application that serves a web page that lists several projects and allows a user to view more
# details about each project.

# Importing the necessary modules from the Flask library
from flask import Flask, render_template, abort

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a list of dictionaries that represent the projects
projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/desk_notebook_pen_glasses.jpg",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://lucos-habit-tracker.onrender.com",
    },
    {
        "name": "Blog Website",
        "thumb": "img/laptop_woman_coffee.jpg",
        "hero": "img/personal-finance.png",
        "categories": ["python", "flask", "web"],
        "slug": "blog-website",
        "prod": "https://lucoblog.onrender.com/",
    },
    {
        "name": "Movie watchlist",
        "thumb": "img/movie_clap.jpg",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

# Creating a dictionary where the keys are the project slugs and the values are the project dictionaries
slug_to_project = {project["slug"]: project for project in projects}

# Defining a route for the homepage
@app.route("/")
def home():
    # Renders the home.html template and passes the projects list to it
    return render_template("home.html", projects=projects)

# Defining a route for the about page
@app.route("/about/")
def about():
    # Renders the about.html template
    return render_template("about.html")

# Defining a route for the contact page
@app.route("/contact/")
def contact():
    # Renders the contact.html template
    return render_template("contact.html")

# Defining a route for the project detail pages
@app.route("/project/<string:slug>")
def project(slug):
    # If the project slug is not in the slug_to_project dictionary, return a 404 error page
    if slug not in slug_to_project:
        abort(404)
    # Renders the project template with the matching slug and passes the project data to it
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

# Defining a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    # Renders the 404.html template and returns a 404 status code
    return render_template("404.html"), 404
