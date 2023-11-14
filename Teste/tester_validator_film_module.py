from Domain.film_module import Film
from Validator.validator_film_module import ValidatorFilm

class TesterValidatorFilm:
    """
    Clasa ce se ocupa cu testele pe validator_film_module
    """
    @staticmethod
    def test_validare_film():
        fl = Film("1", "", "Test")
        valid = ValidatorFilm()
        try:
            valid.validare_film(fl)
            assert False
        except ValueError:
            assert True

        fl = Film("1", "Test", "Test")
        try:
            valid.validare_film(fl)
            assert True
        except ValueError:
            assert False

    @staticmethod
    def test_validare_modificator():
        valid = ValidatorFilm()
        modificator = ""
        try:
            valid.validare_modificator(modificator)
            assert False
        except ValueError:
            assert True

    def teste_validator_film(self):
        self.test_validare_film()
        self.test_validare_modificator()
