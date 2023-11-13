from Domain.film_module import Film
class ValidatorFilm:
    @classmethod
    def validare_film(cls, fl):
        """
            Validare film
            fl - film
            raise ValueError
            if: id, titlu sau gen gol
        """
        erori = ""
        if fl.get_id() == "":
            erori += "Id-ul nu poate fi gol!"
        if fl.get_titlu() == "":
            erori += "Titlul nu poate fi gol!"
        if fl.get_gen() == "":
            erori += "Genul nu poate fi gol!"
        if len(erori) > 0:
            raise ValueError(erori)

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


test_validare_film()
