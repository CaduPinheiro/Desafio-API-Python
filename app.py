from flask import Flask
from flask_restful import Api
from model.movie import MovieModel
from model.serie import SerieModel
from resources.movies import Movie, MovieTitle
from resources.series import Serie, SerieTitle
from services.database import MyDatabase, MyDatabaseSerie
#from resources.comments import Comment

app = Flask(__name__)
api = Api(app)

database = MyDatabase()
MovieModel.database_service = database

database = MyDatabaseSerie()
SerieModel.database_service = database

api.add_resource(Movie, "/movie/<int:id>" , "/movie")
api.add_resource(MovieTitle, "/movie/title/<string:title>" , "/movie/title")
api.add_resource(Serie, "/serie/<int:id>" , "/serie")
api.add_resource(SerieTitle, "/serie/title/<string:title>" , "/serie/title")


if __name__ == '__main__':
    app.run(debug=True)
