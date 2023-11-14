from Domain.client_module import Client

class TesterClient:
    """
    clasa ce se ocupa cu testle pe client_module
    """
    @staticmethod
    def test_creare_client():
        cl = Client("1", "Potra", "Darius")
        assert cl.get_id() == "1"
        assert cl.get_nume() == "Potra"
        assert cl.get_prenume() == "Darius"
