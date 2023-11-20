from Domain.film_module import Film
import random
import string


class ServiceFilm:
    """
    Clasa care se ocupa cu cerintele date pe lista de filme
    """

    def __init__(self, repo, repo_client, validator):
        self.rep = repo
        self.rep_client = repo_client
        self.validator = validator

    @classmethod
    def creare_din_fisier_film(cls, string):
        """
        creeaza un film dintr-un string dat
        :param string:
        :return: fl - Film()
        :raise: ValueError daca string este gol
        """
        if string == "":
            raise ValueError("Nu se poate crea un film!")
        string_despartit = string.split('-')
        id = string_despartit[0]
        titlu = string_despartit[1]
        gen = string_despartit[2]
        nr_fl_inchiriate = int(string_despartit[3])
        inchiriat = string_despartit[4]
        fl = Film(id, titlu, gen)
        fl.set_nr_inchirieri(nr_fl_inchiriate)
        if inchiriat == "True":
            fl.set_inchiriat(True)
        elif inchiriat == "False":
            fl.set_inchiriat(False)

        return fl

    def load_from_file_to_repository_film(self):
        """
        Se incarca dintr-un fisier txt in repository_film o lista cu filme date
        :return:
        """
        file_path = './DataBase/filme_database.txt'
        file = open(file_path, "r")
        for line in file:
            line = line.rstrip('\n')
            cl = self.creare_din_fisier_film(line)
            if self.validator is not None:
                self.validator.validare_film(cl)
            self.rep.store_film(cl)
        file.close()

    def load_film(self, i):
        """
        se creeaza un string dintr-un film dat pentru a fi pus intr-un fisier txt
        :param i: dict.key
        :return: string
        """
        return (self.rep.filme[i].get_id() + "-" + self.rep.filme[i].get_titlu()
                + "-" + self.rep.filme[i].get_gen()
                + "-" + str(self.rep.filme[i].get_nr_inchirieri())
                + "-" + str(self.rep.filme[i].get_inchiriat()))

    def load_from_repository_film_to_file(self):
        """
        Se pune din repository_film intr-un fisier txt
        :return:
        """
        file_path = './DataBase/filme_database.txt'
        file = open(file_path, "w")
        for i in self.rep.filme:
            string = self.load_film(i)
            file.write(string + '\n')
        file.close()

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

    def inchiriere_film(self, id, id_client):
        """
        Functie care se ocupa cu inchirierea unui film
        raise ValueError daca nu exista film cu id-ul dat sau daca filmul este inchiriat deja
                              nu exista un client cu id-ul dat
        """
        if id_client not in self.rep_client.clienti:
            raise IndexError("Nu exista un client cu acest id!")
        if id not in self.rep.filme:
            raise IndexError("Nu exista un film cu acest id!")
        if self.rep.filme[id].get_inchiriat() is True:
            raise ValueError("Filmul este inchiriat deja!")
        self.rep.filme[id].set_inchiriat(True)
        self.rep.filme[id].creste_nr_inchirieri()
        self.rep_client.clienti[id_client].creste_nr_filme_inchiriate()

    def returnare_film(self, id):
        """
        Functie care se ocupa cu returnarea unui film
        raise ValueError daca nu exista un film cu id-ul dat sau daca filmul nu este inchiriat
        """
        if id not in self.rep.filme:
            raise IndexError("Nu exista un film cu acest id!")
        if self.rep.filme[id].get_inchiriat() is False:
            raise ValueError("Filmul nu este inchiriat!")
        self.rep.filme[id].set_inchiriat(False)

    def afisare_film(self, i):
        """
        creeaza si returneaza un string format dintr-un film
        :param i:
        :return: string
        """
        return (str(self.rep.filme[i].get_id()) + " " + str(self.rep.filme[i].get_titlu()) + " "
                + str(self.rep.filme[i].get_gen()))

    def afisare_lista_filme(self):
        """
        se afiseaza toata lista de filme
        :return:
        """
        if self.rep.filme == {}:
            raise ValueError("Lista de filme este goala!")
        for i in self.rep.filme:
            string = self.afisare_film(i)
            print(string)

    @classmethod
    def afisare_rezultat_cautare_filme(cls, dict):
        """
        se afiseaza fiecare element dintr-un dictionar creat din rezultatul unei cautari pe lista de filme
        :param dict:
        :return:
        """
        for i in dict:
            string = dict[i].get_id() + " " + dict[i].get_titlu() + " " + dict[i].get_gen()
            print(string)

    def cautare_filme_dupa_titlu(self, titlu):
        """
        cauta in lista de filme toate filmele cu un titlu dat
        :param titlu:
        :return: dict - dictionar
        """
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_titlu() == titlu:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_dupa_gen(self, gen):
        """
        cauta in lista de filme toate filmele cu un gen dat
        :param gen:
        :return: dict - dictionar
        """
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_gen() == gen:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_de_inchiriat(self):
        """
        cauta in lista de filme toate filmele ce pot fi inchiriate
        :return: dict - dictionar
        """
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_inchiriat() is False:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_inchiriate(self):
        """
        cauta in lista de filme toate filmele inchiriate
        :return: dict - dictionar
        """
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_inchiriat() is True:
                dict[i] = self.rep.filme[i]
        return dict

    @classmethod
    def afisare_cele_mai_inchiriate_filme(cls, dict):
        """
        se afiseaza toate filmele dintr-un dictionar format din cele mai inchiriate filme
        :param dict:
        :return:
        """
        for i in dict:
            string = (dict[i].get_id() + " " + dict[i].get_titlu() + " " + dict[i].get_gen() + " Nr inchirieri:  "
                      + str(dict[i].get_nr_inchirieri()))
            print(string)

    def cele_mai_inchiriate_filme(self):
        """
        Cauta cele mai inchiriate filme
        :return: dict - dictionar
        """
        dict = {}
        max_nr_inchirieri = 0
        for i in self.rep.filme:
            if self.rep.filme[i].get_nr_inchirieri() > max_nr_inchirieri:
                max_nr_inchirieri = self.rep.filme[i].get_nr_inchirieri()

        for i in self.rep.filme:
            if self.rep.filme[i].get_nr_inchirieri() == max_nr_inchirieri:
                dict[i] = self.rep.filme[i]

        return dict

    def generare_random_filme(self, x):
        for i in range(0, x):
            id = ''.join(random.choices(string.digits, k=2))
            titlu = ''.join(random.choices(string.ascii_letters, k=10))
            gen = ''.join(random.choices(string.ascii_letters, k=7))
            print(id + " " + " " + titlu + " " + gen)
            self.add_film(id, titlu, gen)
