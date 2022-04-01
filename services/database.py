import sqlite3


class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("movie_archive.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        create_movie_table = "CREATE TABLE IF NOT EXISTS movie (movie_id INTEGER PRIMARY KEY, title text, \
            sinopse text, genre text, avaliation REAL, year INTEGER)"
        self._cursor.execute(create_movie_table)
        self._db_connection.commit()

    def create_movie(self, movie):
        create_movie_SQL = "INSERT INTO movie VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(movie.id, movie.title, movie.sinopse, movie.genre, movie.avaliation, movie.year)
        self._cursor.execute(create_movie_SQL)
        self._db_connection.commit()

    def list_movies(self):
        list_movies_SQL = "SELECT * from movie;"
        return self._cursor.execute(list_movies_SQL).fetchall()

    def delete_movie(self, movie):
        delete_movie_SQL = "DELETE FROM movie WHERE movie_id='{}'".format(movie.id)
        self._cursor.execute(delete_movie_SQL)
        self._db_connection.commit()

    def find_movie(self, movie_id):
        select_movie_SQL = "SELECT * FROM movie WHERE movie_id='{}'".format(movie_id)
        return self._cursor.execute(select_movie_SQL).fetchone()
    
    def find_filter(self, movie_title):
        select_movie_by_title_SQL = "SELECT * FROM movie WHERE title like '%{}%'".format(movie_title)
        return self._cursor.execute(select_movie_by_title_SQL).fetchone()

    def edit_movie(self, movie):
        edit_movie_SQL = """UPDATE movie SET 
                        title = '{}' 
                        sinopse = '{}' 
                        genre = '{}' 
                        avaliation ='{}' 
                        year = '{}' 
                        WHERE movie_id='{}'""".format(movie.title, movie.sinopse, movie.genre,
                                                movie.avaliation, movie.year, movie.id)
        self._cursor.execute(edit_movie_SQL)
        self._db_connection.commit()

        def __del__(self):
            self._db_connection.close()

class MyDatabaseSerie:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("series_archive.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        create_series_table = "CREATE TABLE IF NOT EXISTS series (series_id integer PRIMARY KEY, title text, sinopse text, genre text, avaliation REAL, seasons INTEGER)"
        self._cursor.execute(create_series_table)
        self._db_connection.commit()
    
    def create_serie(self, series):
        create_series_SQL = "INSERT INTO series VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(series.id, series.title, series.sinopse, series.genre, series.avaliation, series.seasons)
        self._cursor.execute(create_series_SQL)
        self._db_connection.commit()

    def list_serie(self):
        list_series_SQL = "SELECT * from series;"
        return self._cursor.execute(list_series_SQL).fetchall()

    def delete_serie(self, series):
        delete_series_SQL = "DELETE FROM series WHERE series_id='{}'".format(series.id)
        self._cursor.execute(delete_series_SQL)
        self._db_connection.commit()

    def find_serie(self, series_id):
        select_series_SQL = "SELECT * FROM series WHERE series_id='{}'".format(series_id)
        return self._cursor.execute(select_series_SQL).fetchone()

    def find_filter(self, series_title):
        select_series_by_title_SQL = "SELECT * FROM series WHERE title like '%{}%'".format(series_title)
        return self._cursor.execute(select_series_by_title_SQL).fetchall()

    def edit_serie(self, series):
        edit_series_SQL = """UPDATE series SET 
                        title = '{}' 
                        sinopse = '{}' 
                        genre = '{}' 
                        avaliation ='{}' 
                        seasons = '{}' 
                        WHERE serie_id='{}'""".format(series.title, series.sinopse, series.genre,
                                                series.avaliation, series.season, series.id)
        self._cursor.execute(edit_series_SQL)
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()
    

    


    
