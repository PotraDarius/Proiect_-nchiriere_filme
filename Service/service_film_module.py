from Domain.film_module import Film
from Validator.validator_film_module import ValidatorFilm
from Repository.repository_film_module import RepositoryFilm

class ServiceFilm:
    """
    Clasa care se ocupa cu cerintele date pe lista de filme
    """
    def __init__(self, repo, validator):
        self.rep = repo
        self.validator = validator

    def add_film(self, id, titlu, gen):
        """
        Creeaza si stocheaza un film in memorie
        id - string
        titlu - string
        gen - string
        """
        fl = Film(id, titlu, gen)
        if self.validator is not None:
            self.validator.validare_film(fl)
        self.rep.store_film(fl)

    def stergere_film(self, id):
        """
        Sterge un film din memorie dupa un id dat
        id - string
        """
        self.rep.delete_film(id)

    def modifica_film(self, optiune, id, modificator):
        """
        Modifica un film dupa o optiune si un id dat
        optiune - int
        id - string
        modificator - string
        """
        self.validator.validare_modificator(modificator)
        if optiune == 1:
            self.rep.modifica_titlu_film(id, modificator)
        elif optiune == 2:
            self.rep.modifica_gen_film(id, modificator)
        else:
            raise ValueError("Optiunea data nu este valida")

    def afisare_lista_filme(self):
        if self.rep.filme == {}:
            raise ValueError("Lista de filme este goala!")
        for i in self.rep.filme:
            string = (str(self.rep.filme[i].get_id()) + " " + str(self.rep.filme[i].get_titlu()) + " "
                      + str(self.rep.filme[i].get_gen()))
            print(string)


def test_add_film():
    rep = RepositoryFilm()
    val = ValidatorFilm()
    service = ServiceFilm(rep, val)
    assert len(rep.filme) == 0
    service.add_film("1", "Se7en", "Thriller")
    assert len(rep.filme) == 1
    try:
        service.add_film("1", "Test", "Test")
        assert False
    except ValueError:
        assert True

    try:
        service.add_film("2", "", "Test")
        assert False
    except ValueError:
        assert True
    service.add_film("2", "The Zodiac", "Thriller")
    assert len(rep.filme) == 2

def test_stergere_film():
    rep = RepositoryFilm()
    val = ValidatorFilm()
    service = ServiceFilm(rep, val)
    service.add_film("1", "Se7en", "Thriller")
    service.add_film("2", "The Zodiac", "Thriller")
    service.add_film("4", "Star Wars", "Science Fiction")
    service.stergere_film("1")
    assert len(rep.filme) == 2
    try:
        service.stergere_film("3")
        assert False
    except ValueError:
        assert True


def test_modifica_film():
    rep = RepositoryFilm()
    val = ValidatorFilm()
    service = ServiceFilm(rep, val)
    service.add_film("1", "Se7en", "Thriller")
    service.add_film("2", "The Zodiac", "Thriller")
    service.add_film("4", "Star Wars", "Science Fiction")
    service.modifica_film(1, "1", "The Box")
    assert rep.filme["1"].get_titlu() == "The Box"
    service.modifica_film(2, "2", "Killer Documentary")
    assert rep.filme["2"].get_gen() == "Killer Documentary"
    try:
        service.modifica_film(3, "2", "Test")
        assert False
    except ValueError:
        assert True

    try:
        service.modifica_film(1, "3", "Test")
        assert False
    except ValueError:
        assert True


def teste_serice_filme():
    test_add_film()
    test_stergere_film()
    test_modifica_film()


teste_serice_filme()
