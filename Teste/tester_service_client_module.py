from Repository.repository_client_module import RepositoryClient
from Validator.validator_client_module import ValidatorClient
from Service.service_client_module import ServiceClient

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
        service.stergere_client("1")
        assert len(rep.clienti) == 2
        try:
            service.stergere_client("3")
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
        service.modificare_client(1, "1", "Potra-Ratiu")
        assert rep.clienti["1"].get_nume() == "Potra-Ratiu"
        service.modificare_client(2, "2", "Andrei")
        assert rep.clienti["2"].get_prenume() == "Andrei"
        try:
            service.modificare_client(3, "3", "Test")
            assert False
        except ValueError:
            assert True
        try:
            service.modificare_client(1, "3", "Test")
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
        assert list(dict.keys()) == ['1', '4']

    @staticmethod
    def test_cautare_clienti_dupa_prenume():
        rep = RepositoryClient()
        val = ValidatorClient()
        service = ServiceClient(rep, val)
        service.add_client("1", "Potra", "Darius")
        service.add_client("2", "Pop", "Mihai")
        service.add_client("4", "Popescu", "Darius")
        dict = service.cautare_clienti_dupa_prenume("Darius")
        assert list(dict.keys()) == ['1', '4']

    def teste_service_client(self):
        self.test_add_client()
        self.test_stergere_client()
        self.test_modificare_client()
        self.test_cautare_clienti_dupa_nume()
        self.test_cautare_clienti_dupa_prenume()
