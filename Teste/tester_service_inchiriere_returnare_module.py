from Domain.inchiriere_returnare_module import InchiriereReturnare
from Domain.client_module import Client
from Domain.film_module import Film
from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
from Service.service_inchiriere_returnare_module import ServiceInchirereReturnare

class TesterServiceInchiriereReturnare:

    @staticmethod
    def test_inchiriere():
        rep_inc_retr = RepositoryInchiriereReturnare()
        rep_cl = RepositoryClient()
        rep_fl = RepositoryFilm()
        val_inc_retr = ValidatorInchiriereReturnare(rep_cl, rep_fl, rep_inc_retr)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, val_inc_retr, rep_cl, rep_fl)

        cl = Client(1, "Potra", "Darius")
        fl = Film("1", "Se7en", "Thriller")

        rep_cl.store_client(cl)
        rep_fl.store_film(fl)
        service_inc_retr.inchiriere(1, "1")
        assert len(rep_inc_retr.inchirieri) == 1
        assert cl.get_nr_filme_inchiriate() == 1
        assert fl.get_nr_inchirieri() == 1
        assert rep_inc_retr.verificare_status_film("1") is True

        try:
            service_inc_retr.inchiriere(1, "2")
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_returnare():
        rep_inc_retr = RepositoryInchiriereReturnare()
        rep_cl = RepositoryClient()
        rep_fl = RepositoryFilm()
        val_inc_retr = ValidatorInchiriereReturnare(rep_cl, rep_fl, rep_inc_retr)
        service_inc_retr = ServiceInchirereReturnare(rep_inc_retr, val_inc_retr, rep_cl, rep_fl)

        cl = Client(1, "Potra", "Darius")
        fl = Film("1", "Se7en", "Thriller")

        rep_cl.store_client(cl)
        rep_fl.store_film(fl)
        service_inc_retr.inchiriere(1, "1")
        assert len(rep_inc_retr.inchirieri) == 1

        service_inc_retr.returnare("1")
        assert len(rep_inc_retr.inchirieri) == 0
        assert rep_inc_retr.verificare_status_film("1") is False

        try:
            service_inc_retr.returnare("1")
            assert False
        except ValueError:
            assert True

    def teste_service_inchiriere_returnare(self):
        self.test_inchiriere()
        self.test_returnare()

