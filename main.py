from random import *
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=["GET"])
def index():
    # choose a movie by invoking our new function
    movie_today = get_random_movie()
    movie_tomorrow = get_random_movie()

    if movie_tomorrow == movie_today:
        movie_tomorrow = get_random_movie()
    else:
        movie_tomorrow = movie_tomorrow

    # build the response string
    content = "<h1>Movie of the Day for Today</h1>\n"
    content += "<ul>\n"
    content += "<li>" + movie_today + "</li>\n"
    content += "</ul>\n"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    content += "<h1>Movie of the Day for Tomorrow</h1>\n"
    content += "<ul>\n"
    content += "<li>" + movie_tomorrow + "</li>\n"
    content += "</ul>\n"

    return content

def get_random_movie():
    movie_list = ['Die Hard', 'Die Hard 2', 'Die Hard With a Vengeance', 'Live Free or Die Hard', 'A Good Day to Die Hard']
    movie = movie_list[randrange(0, 4, 1)]
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    return movie


app.run()