from Domain.inchiriere_returnare_module import InchiriereReturnare
class ServiceInchirereReturnare:
    """
    Clasa ce se ocupa cu service ul pentru InchiriereReturnare
    """

    def __init__(self, rep_inchirere_returnare, val_inchiriere_returnare, rep_cl, rep_fl):
        self.rep_inc_retr = rep_inchirere_returnare
        self.val_inc_retr = val_inchiriere_returnare
        self.rep_cl = rep_cl
        self.rep_fl = rep_fl

    def inchiriere(self, id_client, id_film):
        """
        Se efectueaza o inchiriere de catre un client si un film
        :param id_client:
        :param id_film:
        :return:
        """

        inchiriare = InchiriereReturnare(id_client, id_film)
        self.val_inc_retr.validare_inchiriere(inchiriare)

        self.rep_inc_retr.store_inchiriere(inchiriare)

        self.rep_fl.filme[id_film].creste_nr_inchirieri()
        self.rep_cl.clienti[id_client].creste_nr_filme_inchiriate()

    def returnare(self, id_film):
        """
        Se returneaza un film dat
        :param id_film:
        :return:
        """
        self.val_inc_retr.validare_returnare(id_film)

        for item in self.rep_inc_retr.inchirieri:
            if item.get_id_film() == id_film:
                self.rep_inc_retr.delete_inchiriere(item)
                break

    def afisare_lista_inchirieri(self):
        """
        Se afiseaza lista de inchirieri
        :return:
        """
        for item in self.rep_inc_retr.inchirieri:
            string = (self.rep_cl.clienti[item.get_id_client()].get_nume() + " "
                      + self.rep_cl.clienti[item.get_id_client()].get_prenume() + " a inchiriat filmul "
                      + self.rep_fl.filme[item.get_id_film()].get_titlu())
            print(string)

    @classmethod
    def creare_din_string_inchiriere(cls, string):
        """
        Creeaza o inchiriere dintr-un string dat
        :param string:
        :return: cl: Client
        """
        string_despartit = string.split(';')
        id_client = int(string_despartit[0])
        id_film = string_despartit[1]
        return InchiriereReturnare(id_client, id_film)

    def load_from_file_to_repository_inchirieri(self):
        """
        :return:
        """
        file_path = './DataBase/inchirieri_database.txt'
        with open(file_path, "r") as file:
            file_lines = file.readlines()
            for line in file_lines:
                line = line.rstrip('\n')
                if line == "":
                    continue
                inc = self.creare_din_string_inchiriere(line)
                if self.val_inc_retr is not None:
                    self.val_inc_retr.validare_inchiriere(inc)
                self.rep_inc_retr.store_inchiriere(inc)

    @classmethod
    def load_inchiriere(cls, item):
        """
        creeaza un string dintr-o inchiriere pentru a fi pus intr-un fisier txt
        :param item: InchiriereReturnare
        :return: string
        """
        return (str(item.get_id_client()) + ";"
                + item.get_id_film())

    def load_from_repository_inchirieri_to_file(self):
        """
        se incarca din repository_inchirieri_returnari lista de clienti intr-un fisier txt
        :return:
        """
        file_path = './DataBase/inchirieri_database.txt'
        with open(file_path, "w") as file:
            for item in self.rep_inc_retr.inchirieri:
                string = self.load_inchiriere(item)
                file.write(string + '\n')
