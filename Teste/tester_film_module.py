from Domain.film_module import Film

class TesterFilm:
    """
    clasa ce se ocupa cu testele pe film_module
    """
    @staticmethod
    def test_creare_film():
        fl = Film("1", "Se7en", "Thriller")
        assert fl.get_id() == "1"
        assert fl.get_titlu() == "Se7en"
        assert fl.get_gen() == "Thriller"
