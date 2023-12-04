from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare

class RepositoryInchiriereReturnare:
    """
    Clasa ce reprezinta un repository al clasei InchiriereReturnare
    """

    def __init__(self):
        self.inchirieri = []

    def store_inchiriere(self, inchiriere):
        """
        Functie care adauga in memorie o inchiriere
        """
        self.inchirieri.append(inchiriere)

    def delete_inchiriere(self, inchiriere):
        """
        Functie care sterge din memorie o inchiriere
        :param inchiriere:
        :return:
        """
        for i in range(0, len(self.inchirieri)):
            if self.inchirieri[i] == inchiriere:
                del self.inchirieri[i]
                break

    def verificare_status_film(self, id_film):
        """
        Functie care verifica daca un film este inchiriat sau nu
        :param id_film:
        :return:
        """
        for item in self.inchirieri:
            if item.get_id_film() == id_film:
                return True
        return False
