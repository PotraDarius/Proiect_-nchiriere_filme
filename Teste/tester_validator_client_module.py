from Domain.client_module import Client
from Validator.validator_client_module import ValidatorClient

class TesterValidatorClient:
    """
    Clasa ce se ocupa cu testele pe validator_client_module
    """
    @staticmethod
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

    @staticmethod
    def test_validare_modificator():
        valid = ValidatorClient()
        modificator = ""
        try:
            valid.validare_modificator(modificator)
            assert False
        except ValueError:
            assert True

    def teste_validator_client(self):
        self.test_validare_client()
        self.test_validare_modificator()
