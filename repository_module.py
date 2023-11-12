from domain_module import Client, Film, Validator
class Repository:
    """
        Clasa ce se ocupa cu stocarea/accesarea de clienti/filme
    """
    def __init__(self):
        self.clienti = {}
        self.filme = {}
        self.__validator = Validator()

    def store_client(self, cl):
        """
        Functie care stocheaza un client in memorie
        cl - client
        raise ValueError daca exista un client cu acelasi id
        """
        if cl.get_id() in self.clienti:
            raise ValueError("Exista deja un client cu acest id!")

        if self.__validator is not None:
            self.__validator.validare_client(cl)

        self.clienti[cl.get_id()] = cl

    def delete_client(self, id):
        """
        Functie care sterge un client din memorie
        cl - client.__id
        raise ValueError daca nu exista un client cu id-ul dat

        """
        if id in self.clienti:
            raise ValueError("Nu exista un client cu id-ul dat")

        del self.clienti[int(id)]

    def store_film(self, fl):
        """
                Functie care stocheaza un film in memorie
                fl - film
                raise ValueError daca exista un film cu acelasi id
        """
        if fl.get_id() in self.filme:
            raise ValueError("Exista deja un film cu acest id!")
        if self.__validator is not None:
            self.__validator.validare_film(fl)

        self.filme[fl.get_id()] = fl

    def delete_film(self, id):
        """
        Functie care sterge un film din memorie
        id - film.__id
        raise ValueError daca nu exista un film cu id-ul dat

        """
        if id in self.filme:
            raise ValueError("Nu exista un client cu id-ul dat")

        del self.filme[int(id)]


def test_store_client():
    cl = Client("1", "Potra", "Darius")
    mem = Repository()
    assert len(mem.clienti) == 0
    mem.store_client(cl)
    assert len(mem.clienti) == 1

    cl = Client("2", "Antonescu", "Marian")
    mem.store_client(cl)
    assert len(mem.clienti) == 2

    cl = Client("2", "Popescu", "Mihai")
    try:
        mem.store_client(cl)
        assert False
    except ValueError:
        assert True


def test_store_film():
    fl = Film("1", "Se7en", "Thriller")
    mem = Repository()
    assert len(mem.filme) == 0
    mem.store_film(fl)
    assert len(mem.filme) == 1

    fl = Film("2", "The Zodiac", "Thriller")
    mem.store_film(fl)
    assert len(mem.filme) == 2

    fl = Film("2", "Star Wars", "Science Fiction")
    try:
        mem.store_film(fl)
        assert False
    except ValueError:
        assert True

def teste_repository():
    test_store_client()
    test_store_film()


teste_repository()
