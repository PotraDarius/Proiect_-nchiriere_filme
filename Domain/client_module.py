class Client:
    """
        Clasa ce reprezinta un client
        Domeniu: id - string
                 nume - string
                 prenume - string
                 lista_filme_inchriate - lista de filme
    """
    def __init__(self, id, nume, prenume):
        self.__id = id
        self.__nume = nume
        self.__prenume = prenume
        self.__numar_filme_inchiriate = 0

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_prenume(self):
        return self.__prenume

    def set_nume(self, nume):
        self.__nume = nume

    def set_prenume(self, prenume):
        self.__prenume = prenume

    def get_nr_filme_inchiriate(self):
        return self.__numar_filme_inchiriate

    def creste_nr_filme_inchiriate(self):
        self.__numar_filme_inchiriate += 1
