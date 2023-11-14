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
        if cl.get_id() == "":
            erori += "Id-ul nu poate fi gol!"
        if cl.get_nume() == "":
            erori += "Numele nu poate fi gol!"
        if cl.get_prenume() == "":
            erori += "Prenumele nu poate fi gol!"
        if len(erori) > 0:
            raise ValueError(erori)

    @classmethod
    def validare_modificator(cls, modificator):
        if modificator == "":
            raise ValueError("Noua valoare nu poate fi goala!")
