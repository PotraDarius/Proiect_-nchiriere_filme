from Domain.client_module import Client
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

    def afisare_client(self, i):
        return (str(self.rep.clienti[i].get_id()) + " " + str(self.rep.clienti[i].get_nume())
                + " " + str(self.rep.clienti[i].get_prenume()))

    def afisare_lista_clienti(self):
        if self.rep.clienti == {}:
            raise ValueError("Lista de clienti este goala!")
        for i in self.rep.clienti:
            string = self.afisare_client(i)
            print(string)

    @classmethod
    def afisare_rezultat_cautare_clienti(cls, dict):
        for i in dict:
            string = dict[i].get_id() + " " + dict[i].get_nume() + " " + dict[i].get_prenume()
            print(string)

    def cautare_clienti_dupa_nume(self, nume):
        dict = {}
        for i in self.rep.clienti:
            if self.rep.clienti[i].get_nume() == nume:
                dict[i] = self.rep.clienti[i]
        return dict

    def cautare_clienti_dupa_prenume(self, prenume):
        dict = {}
        for i in self.rep.clienti:
            if self.rep.clienti[i].get_prenume() == prenume:
                dict[i] = self.rep.clienti[i]
        return dict
