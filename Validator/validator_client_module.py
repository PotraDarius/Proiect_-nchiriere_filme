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

def test_validare_client():
    cl = Client("", "Test", "Test")
    valid = ValidatorClient()
    try:
        valid.validare_client(cl)
        assert False
    except ValueError:
        assert True

    cl = Client("1", "", "Test")
    try:
        valid.validare_client(cl)
        assert False
    except ValueError:
        assert True

    cl = Client("1", "Test", "")
    try:
        valid.validare_client(cl)
        assert False
    except ValueError:
        assert True

    cl = Client("1", "Test", "Test")
    try:
        valid.validare_client(cl)
        assert True
    except ValueError:
        assert False


test_validare_client()
