from Domain.client_module import Client
from Repository.repository_film_module import RepositoryFilm
from Repository.repository_client_module import RepositoryClient
from Validator.validator_film_module import ValidatorFilm
from Service.service_film_module import ServiceFilm
from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare
from Service.service_inchiriere_returnare_module import ServiceInchirereReturnare

class TesterServiceFilm:
    """
    Clasa ce se ocupa cu testele pe service_film_module
    """
    @staticmethod
    def test_add_film():
        rep = RepositoryFilm()
        val = ValidatorFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        service = ServiceFilm(rep, rep_client, rep_inc_retr, val)
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

    @staticmethod
    def test_stergere_film():
        rep = RepositoryFilm()
        val = ValidatorFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        service = ServiceFilm(rep, rep_client, rep_inc_retr, val)
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

    @staticmethod
    def test_modifica_film():
        rep = RepositoryFilm()
        val = ValidatorFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        service = ServiceFilm(rep, rep_client, rep_inc_retr,  val)
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

    @staticmethod
    def test_cautare_filme_dupa_titlu():
        rep = RepositoryFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        service = ServiceFilm(rep, rep_client, rep_inc_retr, valid)
        service.add_film("1", "Se7en", "Thriller")
        service.add_film("2", "The Zodiac", "Thriller")
        dict = service.cautare_filme_dupa_titlu("Se7en")
        assert list(dict.keys()) == ['1']

    @staticmethod
    def test_cautare_filme_dupa_gen():
        rep = RepositoryFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        service = ServiceFilm(rep, rep_client, rep_inc_retr, valid)
        service.add_film("1", "Se7en", "Thriller")
        service.add_film("2", "The Zodiac", "Thriller")
        dict = service.cautare_filme_dupa_gen("Thriller")
        assert list(dict.keys()) == ['1', '2']

    @staticmethod
    def test_cautare_filme_de_inchiriat():
        rep = RepositoryFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        valid_inc_retr = ValidatorInchiriereReturnare(rep_client, rep, rep_inc_retr)
        service = ServiceFilm(rep, rep_client, rep_inc_retr, valid)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, valid_inc_retr, rep_client, rep)
        rep_client.store_client(Client("1", "Potra", "Darius"))
        service.add_film("1", "Se7en", "Thriller")
        service.add_film("2", "The Zodiac", "Thriller")
        service.add_film("3", "Star Wars", "Science Fiction")
        service_inc_retr.inchiriere(1, "2")
        dict = service.cautare_filme_de_inchiriat()
        assert list(dict.keys()) == ['1', '3']

    @staticmethod
    def test_cautare_filme_inchiriate():
        rep = RepositoryFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        valid_inc_retr = ValidatorInchiriereReturnare(rep_client, rep, rep_inc_retr)
        service = ServiceFilm(rep, rep_client, rep_inc_retr, valid)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, valid_inc_retr, rep_client, rep)
        rep_client.store_client(Client("1", "Potra", "Darius"))
        service.add_film("1", "Se7en", "Thriller")
        service.add_film("2", "The Zodiac", "Thriller")
        service.add_film("3", "Star Wars", "Science Fiction")
        service_inc_retr.inchiriere(1, "2")
        dict = service.cautare_filme_inchiriate()
        assert list(dict.keys()) == ['2']

    @staticmethod
    def test_cele_mai_inchiriate_filme():
        rep = RepositoryFilm()
        rep_client = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid_inc_retr = ValidatorInchiriereReturnare(rep_client, rep, rep_inc_retr)
        valid = ValidatorFilm()
        service = ServiceFilm(rep, rep_client, rep_inc_retr, valid)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, valid_inc_retr, rep_client, rep)
        rep_client.store_client(Client("1", "Potra", "Darius"))
        rep_client.store_client(Client("2", "Bucur", "Victor"))
        service.add_film("1", "Se7en", "Thriller")
        service.add_film("2", "The Zodiac", "Thriller")
        service.add_film("3", "Star Wars", "Science Fiction")
        service_inc_retr.inchiriere(1, "1")
        service_inc_retr.inchiriere(2, "2")
        dict = service.cele_mai_inchiriate_filme()
        assert list(dict.keys()) == ['1', '2']

    @staticmethod
    def test_generare_filme_random():
        rep = RepositoryFilm()
        rep_cl = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        service = ServiceFilm(rep, rep_cl, rep_inc_retr, valid)
        service.generare_random_filme(3)
        assert len(rep.filme) == 3

    @staticmethod
    def test_ordonare_filme_dupa_nr_inchirieri():
        rep = RepositoryFilm()
        rep_cl = RepositoryClient()
        rep_inc_retr = RepositoryInchiriereReturnare()
        valid = ValidatorFilm()
        service = ServiceFilm(rep, rep_cl, rep_inc_retr, valid)
        service.add_film("1", "Se7en", "Thriller")
        rep.filme['1'].set_nr_inchirieri(2)
        service.add_film("2", "Zodiac", "Thriller")
        rep.filme['2'].set_nr_inchirieri(3)
        service.add_film("3", "Star Wars", "Science Fiction")
        rep.filme['3'].set_nr_inchirieri(2)
        service.add_film("4", "Die Hard", "Action")
        rep.filme['4'].set_nr_inchirieri(3)
        dict = service.ordonare_filme_dupa_nr_inchirieri()
        assert list(dict.keys()) == ['4', '2', '1', '3']
        rep.filme['3'].set_titlu("Lord of the Rings")
        dict = service.ordonare_filme_dupa_nr_inchirieri()
        assert list(dict.keys()) == ['4', '2', '3', '1']

    def teste_serice_filme(self):
        self.test_add_film()
        self.test_stergere_film()
        self.test_modifica_film()
        self.test_cautare_filme_dupa_titlu()
        self.test_cautare_filme_dupa_gen()
        self.test_cautare_filme_de_inchiriat()
        self.test_cautare_filme_inchiriate()
        self.test_cele_mai_inchiriate_filme()
        self.test_generare_filme_random()
        self.test_ordonare_filme_dupa_nr_inchirieri()
