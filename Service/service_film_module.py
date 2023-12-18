from Domain.film_module import Film
import random
import string


class ServiceFilm:
    """
    Clasa care se ocupa cu cerintele date pe lista de filme
    """

    def __init__(self, repo, repo_client, repo_inc_retr, validator):
        self.rep = repo
        self.rep_client = repo_client
        self.rep_inc_retr = repo_inc_retr
        self.validator = validator

    @classmethod
    def creare_din_fisier_film(cls, string):
        """
        creeaza un film dintr-un string dat
        :param string:
        :return: fl - Film()
        :raise: ValueError daca string este gol
        """
        string_despartit = string.split(',')
        id = string_despartit[0]
        titlu = string_despartit[1]
        gen = string_despartit[2]
        nr_fl_inchiriate = int(string_despartit[3])
        fl = Film(id, titlu, gen)
        fl.set_nr_inchirieri(nr_fl_inchiriate)

        return fl

    def load_from_file_to_repository_film(self):
        """
        Se incarca dintr-un fisier txt in repository_film o lista cu filme date
        :return:
        """
        file_path = './DataBase/filme_database.txt'
        with open(file_path, "r") as file:
            file_lines = file.readlines()
            for line in file_lines:
                line = line.rstrip('\n')
                if line == "":
                    continue
                cl = self.creare_din_fisier_film(line)
                if self.validator is not None:
                    self.validator.validare_film(cl)
                self.rep.store_film(cl)

    def load_film(self, i):
        """
        se creeaza un string dintr-un film dat pentru a fi pus intr-un fisier txt
        :param i: dict.key
        :return: string
        """
        return (self.rep.filme[i].get_id() + "," + self.rep.filme[i].get_titlu()
                + "," + self.rep.filme[i].get_gen()
                + "," + str(self.rep.filme[i].get_nr_inchirieri()))

    def load_from_repository_film_to_file(self):
        """
        Se pune din repository_film intr-un fisier txt
        :return:
        """
        file_path = './DataBase/filme_database.txt'
        with open(file_path, "w") as file:
            for i in self.rep.filme:
                string = self.load_film(i)
                file.write(string + '\n')

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

    def afisare_film(self, i):
        """
        creeaza si returneaza un string format dintr-un film
        :param i:
        :return: string
        """
        return (str(self.rep.filme[i].get_id()) + " " + str(self.rep.filme[i].get_titlu()) + " "
                + str(self.rep.filme[i].get_gen()) + " Nr inchirieri: " + str(self.rep.filme[i].get_nr_inchirieri()))

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

    def afisare_rezultat_cautare_filme(self, dict, lista):
        """
        se afiseaza fiecare element dintr-un dictionar creat din rezultatul unei cautari pe lista de filme
        :param dict:
        :return:
        """
        if lista:
            string = dict[lista[0]].get_id() + " " + dict[lista[0]].get_titlu() + " " + dict[lista[0]].get_gen()
            print(string)
            self.afisare_rezultat_cautare_filme(dict, lista[1:])
        else:
            return

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
            if self.rep_inc_retr.verificare_status_film(i) is False:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_inchiriate(self):
        """
        cauta in lista de filme toate filmele inchiriate
        :return: dict - dictionar
        """
        dict = {}
        for i in self.rep.filme:
            if self.rep_inc_retr.verificare_status_film(i) is True:
                dict[i] = self.rep.filme[i]
        return dict

    @classmethod
    def afisare_rapoarte_filme(cls, dict):
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
            self.add_film(id, titlu, gen)

    @classmethod
    def __bingo_sort(cls, lista, reverse=False, key=lambda x: x[1].get_nr_inchirieri()):
        if not lista:
            return lista
        bingo = key(lista[0])
        max_val = key(lista[0])
        for i in range(1, len(lista)):
            if key(lista[i]) < bingo:
                bingo = key(lista[i])
            if key(lista[i]) > max_val:
                max_val = key(lista[i])

        urm_bingo = max_val
        urm_pos = 0
        while bingo < urm_bingo:
            start_pos = urm_pos

            for i in range(start_pos, len(lista)):
                if key(lista[i]) == bingo:
                    lista[i], lista[urm_pos] = lista[urm_pos], lista[i]
                    urm_pos += 1
                elif key(lista[i]) < urm_bingo:
                    urm_bingo = key(lista[i])

            bingo = urm_bingo
            urm_bingo = max_val

        return lista if reverse is False else lista[::-1]

    def __bingo_sort_filme(self, filme, reverse=False, key=lambda x: x[1].get_nr_inchirieri()):
        items = list(filme.items())
        sorted_items = self.__bingo_sort(items, reverse, key)
        return dict(sorted_items)

    def ordonare_filme_dupa_nr_inchirieri(self):
        dict = self.__bingo_sort_filme(self.rep.filme, True, key=lambda x: x[1].get_nr_inchirieri())
        lista = list(dict.items())
        nr_curent_inchirieri = lista[1][1].get_nr_inchirieri()
        lista_sorted = []
        lista_aux = []

        for item in lista:
            if item[1].get_nr_inchirieri() == nr_curent_inchirieri:
                lista_aux.append(item)
            if item[1].get_nr_inchirieri() != nr_curent_inchirieri:
                lista_aux = self.__bingo_sort(lista_aux, key=lambda x: x[1].get_titlu())
                lista_sorted.extend(lista_aux)
                lista_aux.clear()
                lista_aux.append(item)
                nr_curent_inchirieri = item[1].get_nr_inchirieri()
        lista_aux = self.__bingo_sort(lista_aux, key=lambda x: x[1].get_titlu())
        lista_sorted.extend(lista_aux)
        lista_aux.clear()
        dict = {k: v for k, v in lista_sorted}
        return dict
