from Domain.client_module import Client
from Validator.validator_client_module import ValidatorClient
from Repository.repository_client_module import RepositoryClient
class ServiceClient:
    """
    Clasa care se ocupa cu cerintele date pe lista de clienti
    """
    def __init__(self, repo, validator):
        self.rep = repo
        self.validator = validator

    def add_client(self, id, nume, prenume):
        """
        Creeaza si stocheaza un client in memorie
        id - string
        nume - string
        prenume - string
        """
        cl = Client(id, nume, prenume)
        if self.validator is not None:
            self.validator.validare_client(cl)

        self.rep.store_client(cl)

    def stergere_client(self, id):
        """
        Sterge un client dat dupa un id
        id - string
        """
        self.rep.delete_client(id)

    def modificare_client(self, optiune, id, modificator):
        """
        Modifica datele unui client dupa o optiune si un id dat
        optiune - int
        modificator - string
        pentru optiune == 1 => se modifica numele clientului
        pentru optiune == 2 => se modifica prenumele clientului
        """
        self.validator.validare_modificator(modificator)
        if optiune == 1:
            self.rep.modifica_nume_client(id, modificator)
        elif optiune == 2:
            self.rep.modifica_prenume_client(id, modificator)
        else:
            raise ValueError("Optiunea data nu este valida")

    def afisare_lista_clienti(self):
        if self.rep.clienti == {}:
            raise ValueError("Lista de clienti este goala!")
        for i in self.rep.clienti:
            string = (str(self.rep.clienti[i].get_id()) + " " + str(self.rep.clienti[i].get_nume())
                      + " " + str(self.rep.clienti[i].get_prenume()))
            print(string)


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


def teste_service_client():
    test_add_client()
    test_stergere_client()
    test_modificare_client()


teste_service_client()
