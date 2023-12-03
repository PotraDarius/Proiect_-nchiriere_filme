from Domain.inchiriere_returnare_module import InchiriereReturnare
from Domain.client_module import Client
from Domain.film_module import Film
from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare

class TesterValidatorInchiriereReturnare:

    @staticmethod
    def test_validare_inchiriere():
        cl = Client(1, "Potra", "Darius")
        fl = Film("1", "Se7en", "Thriller")
        inchiriere = InchiriereReturnare(1, "1")
        rep_inc_retr = RepositoryInchiriereReturnare()
        rep_cl = RepositoryClient()
        rep_fl = RepositoryFilm()
        val_inc_retr = ValidatorInchiriereReturnare(rep_cl, rep_fl, rep_inc_retr)
        rep_cl.store_client(cl)
        rep_fl.store_film(fl)
        try:
            val_inc_retr.validare_inchiriere(inchiriere)
            rep_inc_retr.store_inchiriere(inchiriere)
        except ValueError:
            assert False

        try:
            val_inc_retr.validare_inchiriere(inchiriere)
            rep_inc_retr.store_inchiriere(inchiriere)
            assert False
        except ValueError:
            rep_inc_retr.delete_inchiriere(inchiriere)
            assert True
        inchiriere = InchiriereReturnare(2, "1")
        try:
            val_inc_retr.validare_inchiriere(inchiriere)
            assert False
        except ValueError:
            assert True

        inchiriere = InchiriereReturnare(1, "2")
        try:
            val_inc_retr.validare_inchiriere(inchiriere)
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_validare_returnare():
        cl = Client(1, "Potra", "Darius")
        fl = Film("1", "Se7en", "Thriller")
        inchiriere = InchiriereReturnare(1, "1")
        rep_inc_retr = RepositoryInchiriereReturnare()
        rep_cl = RepositoryClient()
        rep_fl = RepositoryFilm()
        val_inc_retr = ValidatorInchiriereReturnare(rep_cl, rep_fl, rep_inc_retr)
        rep_cl.store_client(cl)
        rep_fl.store_film(fl)

        try:
            val_inc_retr.validare_returnare("1")
            assert False
        except ValueError:
            assert True

        try:
            val_inc_retr.validare_returnare("2")
            assert False
        except IndexError:
            assert True

        rep_inc_retr.store_inchiriere(inchiriere)
        try:
            val_inc_retr.validare_returnare("1")
        except ValueError:
            assert False

    def teste_validator_inchiriere_returnare(self):
        self.test_validare_inchiriere()
        self.test_validare_returnare()
