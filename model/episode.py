from services.database import MyDatabaseSerie

class EpisodeModel:
    database_service: MyDatabaseSerie = None
    def __init__(self, title, sinopse, season, id=None) -> None:
        if id:
            self.id = id
        else:
            highest_id = int(max(self.seek_existing_ids())) if self.seek_existing_ids() else 0
            self.id = highest_id + 1
        self.title = title
        self.sinopse = sinopse
        self.season = season

    @classmethod
    def seek_existing_ids(cls):
        result = cls.database_service.list_serie()
        id_list = []
        for serie in result:
            id_list.append(serie[0])
        return sorted(id_list)    