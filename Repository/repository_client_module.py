from Domain.client_module import Client
from Validator.validator_client_module import ValidatorClient
class RepositoryClient:
    """
        Clasa ce se ocupa cu stocarea/accesarea de clienti/filme
    """
    def __init__(self):
        self.clienti = {}
        self.__validator = ValidatorClient()

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

    def validare_id(self, id):
        if id not in self.clienti.keys():
            raise ValueError("Nu exista un client cu id-ul dat")

    def delete_client(self, id):
        """
        Functie care sterge un client din memorie
        cl - client.__id
        raise ValueError daca nu exista un client cu id-ul dat

        """
        self.validare_id(id)
        del self.clienti[id]

    def modifica_nume_client(self, id, nume):
        self.validare_id(id)
        self.clienti[id].set_nume(nume)

    def modifica_prenume_client(self, id, prenume):
        self.validare_id(id)
        self.clienti[id].set_prenume(prenume)


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


def test_delete_client():
    cl = Client("1", "Test", "Test")
    rep = RepositoryClient()
    rep.store_client(cl)
    cl = Client("2", "Test", "Test")
    rep.store_client(cl)
    assert len(rep.clienti) == 2
    rep.delete_client("1")
    assert len(rep.clienti) == 1
    try:
        rep.delete_client("3")
        assert False
    except ValueError:
        assert True


def teste_repository_client():
    test_store_client()
    test_delete_client()


teste_repository_client()
