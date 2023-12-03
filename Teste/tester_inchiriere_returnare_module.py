from Domain.inchiriere_returnare_module import InchiriereReturnare

class TesterInchiriereReturnare:

    @staticmethod
    def test_inchiriere_returnare():
        inchiriere1 = InchiriereReturnare(2, "3")
        inchiriere2 = InchiriereReturnare(3, "4")

        assert inchiriere1.get_id_film() == "3"
        assert inchiriere1.get_id_client() == 2
        try:
            assert inchiriere1 == inchiriere2
            assert False
        except AssertionError:
            assert True
