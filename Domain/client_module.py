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
        self.__lista_filme_inchiriate = []

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


def test_creare_client():
    cl = Client("1", "Potra", "Darius")
    assert cl.get_id() == "1"
    assert cl.get_nume() == "Potra"
    assert cl.get_prenume() == "Darius"


test_creare_client()
