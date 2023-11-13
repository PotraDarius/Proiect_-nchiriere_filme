class ValidatorUI:
    """
    Clasa ce se ocupa cu validarea datelor de intrare date de utilizator

    """
    @classmethod
    def validare_optiune(cls, p):
        """
        Functie care valideaza un numar dat pentru a if o optiune
        p - int
        raise ValueaError daca p <= 0
        """
        if p == '' or int(p) <= 0:
            raise ValueError("Alegerea data nu este valida")
        else:
            return True


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


test_validare_optiune()
