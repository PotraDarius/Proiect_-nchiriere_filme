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
