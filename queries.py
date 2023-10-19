# pylint: disable=C0103, missing-docstring
import sqlite3

# conn = sqlite3.connect('data/movies.sqlite')
# db = conn.cursor()
# db.execute("YOUR SQL QUERY")
# rows = db.fetchall()
# print(rows)


def connect_to_database():
    # create connection to sql databate
    # initialize cursor
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    return conn,  db


def close_database(conn):
    # close database connection
    conn.close()


def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    conn, db = connect_to_database()
    db.execute(
        "SELECT title, genres, name\
            FROM movies \
            JOIN directors\
            ON movies.director_id = directors.id"
        )
    rows = db.fetchall()
    close_database(conn)
    return rows
    


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    pass  # YOUR CODE HERE


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    pass  # YOUR CODE HERE


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    pass  # YOUR CODE HERE


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    pass  # YOUR CODE HERE
