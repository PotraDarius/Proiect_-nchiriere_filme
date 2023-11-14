from Validator.validator_UI_module import ValidatorUI

class TesterValidatorUI:
    """
    Clasa ce se ocupa cu testele pe validator_UI_module
    """
    @staticmethod
    def test_validare_optiune():
        p = 5
        validator = ValidatorUI()
        assert validator.validare_optiune(p) is True
        p = -3
        try:
            validator.validare_optiune(p)
            assert False
        except ValueError:
            assert True
