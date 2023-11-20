from Domain.client_module import Client
from Repository.repository_client_module import RepositoryClient

class TesterRepoClient:
    """
    Clasa ce se ocupa cu testele pentru repository_client_module
    """
    @staticmethod
    def test_store_client():
        cl = Client("1", "Potra", "Darius")
        mem = RepositoryClient()
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

    @staticmethod
    def test_delete_client():
        cl = Client("1", "Test", "Test")
        rep = RepositoryClient()
        rep.store_client(cl)
        cl = Client("2", "Test", "Test")
        rep.store_client(cl)
        assert len(rep.clienti) == 2
        rep.delete_client(1)
        assert len(rep.clienti) == 1
        try:
            rep.delete_client(3)
            assert False
        except ValueError:
            assert True

    def teste_repository_client(self):
        self.test_store_client()
        self.test_delete_client()
