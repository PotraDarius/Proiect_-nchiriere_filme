from Domain.inchiriere_returnare_module import InchiriereReturnare
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
class ValidatorInchiriereReturnare:
    """
    Clasa ce se ocupa cu validari pentru InchiriereReturnare
    """

    def __init__(self, rep_cl, rep_fl, rep_inc_retr):
        self.__rep_cl = rep_cl
        self.__rep_fl = rep_fl
        self.__rep_inc_retr = rep_inc_retr

    def validare_inchiriere(self, inchiriere):
        """
        Functie ce valideaza o inchiriere
        :param inchiriere:
        :return:
        """
        erori = ""
        if inchiriere.get_id_client() not in self.__rep_cl.clienti:
            erori += "Nu exista un client cu id-ul dat! "

        if inchiriere.get_id_film() not in self.__rep_fl.filme:
            erori += "Nu exista un film cu id-ul dat! "
        elif inchiriere in self.__rep_inc_retr.inchirieri:
            erori += "Filmul este inchiriat deja! "

        if erori != "":
            raise ValueError(erori)

    def validare_returnare(self, id_film):
        """
        Functie ce valideaza o returnare
        :param id_film:
        :return:
        """
        if id_film not in self.__rep_fl.filme:
            raise IndexError("Nu exista un film cu acest id!")
        ok = 0
        for item in self.__rep_inc_retr.inchirieri:
            if item.get_id_film() == id_film:
                ok = 1
                break
        if ok == 0:
            raise ValueError("Filmul dat nu este inchiriat!")


