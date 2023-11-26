from Domain.client_module import Client
import random
import string
class ServiceClient:
    """
    Clasa care se ocupa cu cerintele date pe lista de clienti
    """
    def __init__(self, repo, validator):
        self.rep = repo
        self.validator = validator

    @classmethod
    def creare_din_string_client(cls, string):
        """
        Creeaza un client dintr-un string dat
        :param string:
        :return: cl: Client
        """
        string_despartit = string.split('-')
        id = int(string_despartit[0])
        nume = string_despartit[1]
        prenume = string_despartit[2]
        nr_fl_inchiriate = int(string_despartit[3])
        cl = Client(id, nume, prenume)
        cl.set_nr_filme_inchiriate(nr_fl_inchiriate)
        return cl

    def load_from_file_to_repository_client(self):
        """
        Se incarca dintr-un fisier txt lista de clienti in repository_client
        :return:
        """
        file_path = './DataBase/clienti_database.txt'
        file = open(file_path, "r")
        for line in file:
            line = line.rstrip('\n')
            if line == "":
                continue
            cl = self.creare_din_string_client(line)
            if self.validator is not None:
                self.validator.validare_client(cl)
            self.rep.store_client(cl)
        file.close()

    def load_client(self, i):
        """
        creeaza un string dintr-un client pentru a fi pus intr-un fisier txt
        :param i: dict.key
        :return: string
        """
        return (str(self.rep.clienti[i].get_id()) + "-" + self.rep.clienti[i].get_nume()
                + "-" + self.rep.clienti[i].get_prenume()
                + "-" + str(self.rep.clienti[i].get_nr_filme_inchiriate()))

    def load_from_repository_client_to_file(self):
        """
        se incarca din repository_client lista de clienti intr-un fisier txt
        :return:
        """
        file_path = './DataBase/clienti_database.txt'
        file = open(file_path, "w")
        for i in self.rep.clienti:
            string = self.load_client(i)
            file.write(string + '\n')
        file.close()

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
        """
        Se returneaza afisarea unui client din repository
        :param i:
        :return: string
        """
        return (str(self.rep.clienti[i].get_id()) + " " + self.rep.clienti[i].get_nume()
                + " " + self.rep.clienti[i].get_prenume()
                + " Nr filme inchiriate: " + str(self.rep.clienti[i].get_nr_filme_inchiriate()))

    def afisare_lista_clienti(self):
        """
        Se afiseaza toti clientii din lista de clienti
        :return:
        """
        if self.rep.clienti == {}:
            raise ValueError("Lista de clienti este goala!")
        for i in self.rep.clienti:
            string = self.afisare_client(i)
            print(string)

    @classmethod
    def afisare_rezultat_cautare_clienti(cls, dict):
        """
        Afiseaza fiecare client dintr-o lista data rezultata din urma unei cautari
        :param dict:
        :return:
        """
        for i in dict:
            string = (str(dict[i].get_id()) + " " + dict[i].get_nume() + " " + dict[i].get_prenume()
                      + " Nr filme inchiriare: " + str(dict[i].get_nr_filme_inchiriate()))
            print(string)

    def cautare_clienti_dupa_nume(self, nume):
        """
        Se cauta si se pun intr-o lista auxiliara toti clientii dupa un nume dat
        :param nume: string
        :return: dict
        """
        dict = {}
        for i in self.rep.clienti:
            if self.rep.clienti[i].get_nume() == nume:
                dict[i] = self.rep.clienti[i]
        return dict

    def cautare_clienti_dupa_prenume(self, prenume):
        """
        Se cauta si se pun intr-o lista auxiliara toti clientii dupa un prenume dat
        :param prenume: string
        :return: dict
        """
        dict = {}
        for i in self.rep.clienti:
            if self.rep.clienti[i].get_prenume() == prenume:
                dict[i] = self.rep.clienti[i]
        return dict

    @classmethod
    def afisare_rezultat_rapoarte_clienti(cls, dict):
        """
        Se afiseaza toti clientii dintr-o lista data rezultate din calcularea unui raport pe lista de clienti
        :param dict: dictionary
        :return:
        """
        for i in dict:
            string = (str(dict[i].get_id()) + " " + dict[i].get_nume() + " " + dict[i].get_prenume()
                      + " Nr filme inchiriare: " + str(dict[i].get_nr_filme_inchiriate()))
            print(string)

    def ordonare_clienti_dupa_nume(self):
        """
        Ordoneaza toti clientii dupa nume intr-o lista auxiliara si este returnata
        :return: ordonate_dict: dicitionary
        """
        ordonate = sorted(self.rep.clienti.items(), key=lambda x: x[1].get_nume())
        ordonate_dict = {k: v for k, v in ordonate}
        return ordonate_dict

    def ordonare_clienti_dupa_nr_filme_inchiriate(self):
        """
        Ordoneaza toti clientii dupa numarul de filme inchiriate intr-o lista auxiliara si este returnata
        :return: ordonate_dict: dicitionary
        """
        ordonate = sorted(self.rep.clienti.items(), key=lambda x: x[1].get_nr_filme_inchiriate(), reverse=True)
        ordonate_dict = {k: v for k, v in ordonate}
        return ordonate_dict

    def generare_random_clienti(self, x):
        for i in range(0, x):
            id = int(''.join(random.choices(string.digits, k=2)))
            titlu = ''.join(random.choices(string.ascii_letters, k=10))
            gen = ''.join(random.choices(string.ascii_letters, k=7))
            print(str(id) + " " + " " + titlu + " " + gen)
            self.add_client(id, titlu, gen)

    def primii_30lasuta_clienti_cu_filme_inchiriate(self):
        ordonate = self.ordonare_clienti_dupa_nr_filme_inchiriate()
        primii_30lasuta = int((30*len(ordonate))/100)
        primii_30lasuta_dict = {}
        if primii_30lasuta == 0:
            primii_30lasuta = 1
        for i in ordonate:
            if primii_30lasuta > 0:
                primii_30lasuta_dict[i] = ordonate[i]
                primii_30lasuta -= 1
        return primii_30lasuta_dict

