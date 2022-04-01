from json import dumps, loads
from services.database import MyDatabaseSerie

class SerieModel:

    database_service: MyDatabaseSerie = None

    def __init__(self, title, sinopse, genre, avaliation, seasons,  id=None) -> None:
        if id:
            self.id = id
        else:
            highest_id = int(max(self.seek_existing_ids())) if self.seek_existing_ids() else 0
            self.id = highest_id + 1
        self.title = title
        self.sinopse = sinopse
        self.genre = genre
        self.avaliation = avaliation
        self.seasons = seasons

    @classmethod
    def add_serie(cls, series):
        cls.database_service.create_serie(series)

    @classmethod
    def find_serie(cls, serie_id):
        found_serie = None
        result = cls.database_service.find_serie(serie_id)
        print(result)
        if result:
            found_serie = SerieModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_serie  

    @classmethod
    def find_serie_by_params(cls, serie_title):
        found_serie = None
        result = cls.database_service.find_filter(serie_title)
        if result:
            found_serie = SerieModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_serie  

    @classmethod
    def remove_serie(cls, serie):
        cls.database_service.delete_serie(serie)
 
    @classmethod
    def list_to_dict(cls):
        result = cls.database_service.list_serie()
        serie_list = []
        for serie in result:
            serie_list.append(SerieModel(serie[1], serie[2], serie[3], serie[4], serie[5], serie[0]))
        return loads(dumps(serie_list, default=SerieModel.to_dict))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "sinopse": self.sinopse,
            "genre": self.genre,
            "avaliation": self.avaliation,
            "seasons": self.seasons
        }

    @classmethod
    def seek_existing_ids(cls):
        result = cls.database_service.list_serie()
        id_list = []
        for serie in result:
            id_list.append(serie[0])
        return sorted(id_list)    




