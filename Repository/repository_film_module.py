from Domain.film_module import Film
from Validator.validator_film_module import ValidatorFilm

class RepositoryFilm:
    """
        Clasa ce se ocupa cu stocarea/accesarea de filme
     """
    def __init__(self):
        self.filme = {}
        self.__validator = ValidatorFilm()

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

    def validare_id(self, id):
        if id not in self.filme.keys():
            raise ValueError("Nu exista un client cu id-ul dat")

    def delete_film(self, id):
        """
        Functie care sterge un film din memorie
        id - film.__id
        raise ValueError daca nu exista un film cu id-ul dat

        """
        self.validare_id(id)
        del self.filme[id]

    def modifica_titlu_film(self, id, titlu):
        self.validare_id(id)
        self.filme[id].set_titlu(titlu)

    def modifica_gen_film(self, id, gen):
        self.validare_id(id)
        self.filme[id].set_gen(gen)

def test_store_film():
    fl = Film("1", "Se7en", "Thriller")
    mem = RepositoryFilm()
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


def test_delete_film():
    fl = Film("1", "Test", "Test")
    rep = RepositoryFilm()
    rep.store_film(fl)
    fl = Film("2", "Test", "Test")
    rep.store_film(fl)
    assert len(rep.filme) == 2
    rep.delete_film("1")
    assert len(rep.filme) == 1
    try:
        rep.delete_film("3")
        assert False
    except ValueError:
        assert True


def teste_repository_filme():
    test_store_film()
    test_delete_film()


teste_repository_filme()
