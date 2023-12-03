
class InchiriereReturnare:
    def __init__(self, id_client, id_film):
        self.__id_client = id_client
        self.__id_film = id_film

    def get_id_client(self):
        return self.__id_client

    def get_id_film(self):
        return self.__id_film

    def __eq__(self, other):
        return self.get_id_client() == other.get_id_client() and self.get_id_film() == other.get_id_film()
