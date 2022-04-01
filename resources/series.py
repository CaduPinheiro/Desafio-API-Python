from flask_restful import Resource, reqparse
from model.serie import SerieModel

class Serie(Resource):
    def get(self, id=None):
        if id:
            found_serie = SerieModel.find_serie(id)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404
        else:
            return SerieModel.list_to_dict()
    
    def get(self, id=None):
        if id:
            found_serie = SerieModel.find_serie(id)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404
        else:
            return SerieModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopse")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("avaliation")
        body_arguments.add_argument("seasons")

        params = body_arguments.parse_args()
        #print(params.cast)
        new_serie = SerieModel(params["title"], params["sinopse"], params["genre"], params["avaliation"], params["seasons"])
        SerieModel.add_serie(new_serie)
        return new_serie.to_dict()

    def delete(self, id):
        found_serie = SerieModel.find_serie(id)
        if found_serie:
            SerieModel.remove_serie(found_serie)
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

    def put(self, id):
        found_serie = SerieModel.find_serie(id)
        if found_serie:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            body_arguments.add_argument("sinopse")
            body_arguments.add_argument("genre")
            body_arguments.add_argument("avaliation")
            body_arguments.add_argument("seasons")
            params = body_arguments.parse_args()
            found_serie.title = params.title
            found_serie.sinopse = params.sinopse
            found_serie.genre = params.genre
            found_serie.avaliation = params.avaliation
            found_serie.seasons = params.seasons
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

class SerieTitle(Resource):
    def get(self, title=None):
        if title:
            found_serie = SerieModel.find_serie_by_params(title)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404
        else:
            return SerieModel.list_to_dict()
