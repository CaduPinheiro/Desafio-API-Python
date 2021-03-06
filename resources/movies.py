from flask_restful import Resource, reqparse
from model.movie import MovieModel

class Movie(Resource):
    def get(self, id=None):
        if id:
            found_movie = MovieModel.find_movie(id)
            if found_movie:
                return found_movie.to_dict()
            return {"message": "Movie not found"}, 404
        else:
            return MovieModel.list_to_dict()
    
    def get(self, id=None):
        if id:
            found_movie = MovieModel.find_movie(id)
            if found_movie:
                return found_movie.to_dict()
            return {"message": "Movie not found"}, 404
        else:
            return MovieModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopse")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("avaliation")
        body_arguments.add_argument("year")

        params = body_arguments.parse_args()
        #print(params.cast)
        new_movie = MovieModel(params["title"], params["sinopse"], params["genre"], params["avaliation"], params["year"])
        MovieModel.add_movie(new_movie)
        return new_movie.to_dict()

    def delete(self, id):
        found_movie = MovieModel.find_movie(id)
        if found_movie:
            MovieModel.remove_movie(found_movie)
            return found_movie.to_dict()
        return {"message": "Movie not found"}, 404

    def put(self, id):
        found_movie = MovieModel.find_movie(id)
        if found_movie:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            body_arguments.add_argument("sinopse")
            body_arguments.add_argument("genre")
            body_arguments.add_argument("avaliation")
            body_arguments.add_argument("year")
            params = body_arguments.parse_args()
            found_movie.title = params.title
            found_movie.sinopse = params.sinopse
            found_movie.genre = params.genre
            found_movie.avaliation = params.avaliation
            found_movie.year = params.year
            return found_movie.to_dict()
        return {"message": "Movie not found"}, 404

class MovieTitle(Resource):
    def get(self, title=None):
        if title:
            found_movie = MovieModel.find_movie_by_params(title)
            if found_movie:
                return found_movie.to_dict()
            return {"message": "Movie not found"}, 404
        else:
            return MovieModel.list_to_dict()
