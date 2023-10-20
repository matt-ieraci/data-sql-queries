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
    conn, db = connect_to_database()
    db.execute(
        "SELECT title\
            FROM movies\
            JOIN directors\
                ON movies.director_id = directors.id\
                WHERE movies.start_year > directors.death_year"
        )
    rows = db.fetchall()
    late_release_list = []
    for row in rows:
        late_release_list.append(row[0])
    close_database(conn)
    return late_release_list


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    conn, db = connect_to_database()
    db.execute(
        f"SELECT genres, COUNT(title), AVG(minutes)\
            FROM movies\
            WHERE genres = '{genre_name}'"
        )
    rows = db.fetchall()
    movie_dict = {}
    for row in rows:
        formatted_avg = f"{row[2]:.2f}"
        movie_dict['genre'] = row[0]
        movie_dict['number_of_movies'] = row[1]
        movie_dict['avg_length'] = float(formatted_avg)
    close_database(conn)
    return movie_dict


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    pass  # YOUR CODE HERE
    #SELECT name FROM directors WHERE movies.genres = 'Action,Adventure,Comedy' JOIN movies ON movies.director_id = directors.id ORDER BY movies.title DESC LIMIT 5 

def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    conn, db = connect_to_database()
    i = 0
    j = 30
    movie_duration_list = []
    while j <= 1020:
        db.execute(
            f"SELECT COUNT(*) FROM movies WHERE minutes > {i} AND minutes < {j}"
            )
        rows = db.fetchall()
        row_tuple = tuple((j, rows[0][0]))
        movie_duration_list.append(row_tuple)
        i += 30
        j += 30
    close_database(conn)
    return movie_duration_list
    


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    conn, db = connect_to_database()
    db.execute(
        '''
        SELECT directors.name, 
            MIN(movies.start_year- directors.birth_year)
            AS age_at_first_movie
        FROM directors
        JOIN movies ON movies.director_id = directors.id
        WHERE directors.birth_year  IS NOT NULL AND movies.start_year IS NOT NULL
        GROUP BY directors.name, directors.id 
        ORDER BY age_at_first_movie
        LIMIT 5
        '''
        )
    rows = db.fetchall()
    top_5_directors = []
    for row in rows:
        top_5_directors.append((row[0], row[1]))
    close_database(conn)
    return top_5_directors
    
