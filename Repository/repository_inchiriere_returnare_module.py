from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare

class RepositoryInchiriereReturnare:

    def __init__(self):
        self.inchirieri = []

    def store_inchiriere(self, inchiriere):
        self.inchirieri.append(inchiriere)

    def delete_inchiriere(self, inchiriere):
        for i in range(0, len(self.inchirieri)):
            if self.inchirieri[i] == inchiriere:
                del self.inchirieri[i]
                break

    def verificare_status_film(self, id_film):
        for item in self.inchirieri:
            if item.get_id_film() == id_film:
                return True
        return False
