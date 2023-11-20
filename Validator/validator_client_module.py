from Domain.client_module import Client
class ValidatorClient:
    """
        Clasa ce se ocupa cu validarea datelor introduse
    """
    @classmethod
    def validare_client(cls, cl):
        """
            Validare client
            cl - Client
            raise ValueError
            if: id, nume sau prenume gol
        """
        erori = ""
        if cl.get_id() <= 0:
            erori += "Id-ul nu poate fi negativ!"
        if cl.get_nume() == "":
            erori += "Numele nu poate fi gol!"
        if cl.get_prenume() == "":
            erori += "Prenumele nu poate fi gol!"
        if len(erori) > 0:
            raise ValueError(erori)

    @classmethod
    def validare_modificator(cls, modificator):
        """
        Validare un string folosit pentru modificarea unui client
        :param modificator:
        :raise Value Error daca modificator este gol
        """
        if modificator == "":
            raise ValueError("Noua valoare nu poate fi goala!")
