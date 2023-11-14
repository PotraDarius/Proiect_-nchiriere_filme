from Domain.film_module import Film

class ServiceFilm:
    """
    Clasa care se ocupa cu cerintele date pe lista de filme
    """
    def __init__(self, repo, repo_client, validator):
        self.rep = repo
        self.rep_client = repo_client
        self.validator = validator

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
        return (str(self.rep.filme[i].get_id()) + " " + str(self.rep.filme[i].get_titlu()) + " "
                      + str(self.rep.filme[i].get_gen()))

    def afisare_lista_filme(self):
        if self.rep.filme == {}:
            raise ValueError("Lista de filme este goala!")
        for i in self.rep.filme:
            string = self.afisare_film(i)
            print(string)

    @classmethod
    def afisare_rezultat_cautare_filme(cls, dict):
        for i in dict:
            string = dict[i].get_id() + " " + dict[i].get_titlu() + " " + dict[i].get_gen()
            print(string)

    def cautare_filme_dupa_titlu(self, titlu):
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_titlu() == titlu:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_dupa_gen(self, gen):
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_gen() == gen:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_de_inchiriat(self):
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_inchiriat() is False:
                dict[i] = self.rep.filme[i]
        return dict

    def cautare_filme_inchiriate(self):
        dict = {}
        for i in self.rep.filme:
            if self.rep.filme[i].get_inchiriat() is True:
                dict[i] = self.rep.filme[i]
        return dict

