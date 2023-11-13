from Service.service_client_module import ServiceClient
from Service.service_film_module import ServiceFilm
class UI:
    """
    Clasa ce va defini o interfata
    """
    def meniu_principal(self):
        while True:
            print("Meniul aplicatiei")
            print("1.Adauga film/client")
            print("2.Sterge film/client")
            print("3.Modifica film/client")
