from Domain.client_module import Client
from Repository.repository_client_module import RepositoryClient
from Validator.validator_client_module import ValidatorClient
from Service.service_client_module import ServiceClient
from Repository.repository_film_module import RepositoryFilm
from Validator.validator_film_module import ValidatorFilm
from Service.service_film_module import ServiceFilm
from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare
from Service.service_inchiriere_returnare_module import ServiceInchirereReturnare

class TesterServiceClient:
    """
    Clasa ce se ocupa cu testele pe service_client module
    """
    @staticmethod
    def test_add_client():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        assert len(rep.clienti) == 0
        service.add_client("1", "Potra", "Darius")
        assert len(rep.clienti) == 1
        try:
            service.add_client("1", "Pop", "Mihai")
            assert False
        except ValueError:
            assert True

        try:
            service.add_client("2", "", "Test")
            assert False
        except ValueError:
            assert True
        service.add_client("2", "Pop", "Mihai")
        assert len(rep.clienti) == 2

    @staticmethod
    def test_stergere_client():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Pop", "Mihai")
        service.add_client("4", "Popescu", "Adrian")
        assert len(rep.clienti) == 3
        service.stergere_client(1)
        assert len(rep.clienti) == 2
        try:
            service.stergere_client(3)
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_modificare_client():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Pop", "Mihai")
        service.add_client("4", "Popescu", "Adrian")
        assert len(rep.clienti) == 3
        service.modificare_client(1, 1, "Potra-Ratiu")
        assert rep.clienti[1].get_nume() == "Potra-Ratiu"
        service.modificare_client(2, 2, "Andrei")
        assert rep.clienti[2].get_prenume() == "Andrei"
        try:
            service.modificare_client(3, 3, "Test")
            assert False
        except ValueError:
            assert True
        try:
            service.modificare_client(1, 3, "Test")
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_cautare_clienti_dupa_nume():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Pop", "Mihai")
        service.add_client("4", "Potra", "Adrian")
        dict = service.cautare_clienti_dupa_nume("Potra")
        assert list(dict.keys()) == [1, 4]

    @staticmethod
    def test_cautare_clienti_dupa_prenume():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Pop", "Mihai")
        service.add_client("4", "Popescu", "Darius")
        dict = service.cautare_clienti_dupa_prenume("Darius")
        assert list(dict.keys()) == [1, 4]

    @staticmethod
    def test_ordonare_clienti_dupa_nume():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Bucur", "Victor")
        dict = service.ordonare_clienti_dupa_nume()
        assert list(dict.keys()) == [2, 1]

    @staticmethod
    def test_ordonare_clienti_dupa_nr_filme_inchiriate():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        rep_fl = RepositoryFilm()
        val_fl = ValidatorFilm()

        rep_inc_retr = RepositoryInchiriereReturnare()
        val_inc_retr = ValidatorInchiriereReturnare(rep, rep_fl, rep_inc_retr)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, val_inc_retr, rep, rep_fl)
        service_fl = ServiceFilm(rep_fl, rep, rep_inc_retr, val_fl)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Bucur", "Victor")
        service_fl.add_film("1", "Seyen", "Thriller")
        service_inc_retr.inchiriere(2, "1")
        dict = service.ordonare_clienti_dupa_nr_filme_inchiriate()
        assert list(dict.keys()) == [2, 1]

    @staticmethod
    def test_generare_clienti_random():
        rep_cl = RepositoryClient()
        valid = ValidatorClient()
        service = ServiceClient(rep_cl, valid)
        service.generare_random_clienti(3)
        assert len(rep_cl.clienti) == 3

    @staticmethod
    def test_primii_30lasuta_clienti():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client(1, "Potra", "Darius")
        rep.clienti[1].set_nr_filme_inchiriate(4)
        service.add_client(2, "Bucur", "Victor")
        rep.clienti[2].set_nr_filme_inchiriate(3)
        service.add_client(3, "Bucur", "Felix")
        rep.clienti[3].set_nr_filme_inchiriate(6)
        service.add_client(4, "Timbus", "Flaviu")
        rep.clienti[4].set_nr_filme_inchiriate(7)
        assert len(rep.clienti) == 4
        dict = service.ordonare_clienti_dupa_nr_filme_inchiriate()
        assert list(dict.keys()) == [4, 3, 1, 2]
        treizeci = service.primii_30lasuta_clienti_cu_filme_inchiriate()
        assert list(treizeci.keys()) == [4]

    def teste_service_client(self):
        self.test_add_client()
        self.test_stergere_client()
        self.test_modificare_client()
        self.test_cautare_clienti_dupa_nume()
        self.test_cautare_clienti_dupa_prenume()
        self.test_ordonare_clienti_dupa_nume()
        self.test_ordonare_clienti_dupa_nr_filme_inchiriate()
        self.test_generare_clienti_random()
        self.test_primii_30lasuta_clienti()
