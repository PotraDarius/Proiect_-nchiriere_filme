from Domain.film_module import Film
from Repository.repository_film_module import RepositoryFilm

class TesterRepoFilm:
    """
    Clasa ce se ocupa cu testele pe repository_film_module
    """
    @staticmethod
    def test_store_film():
        fl = Film("1", "Se7en", "Thriller")
        mem = RepositoryFilm()
        assert len(mem.filme) == 0
        mem.store_film(fl)
        assert len(mem.filme) == 1

        fl = Film("2", "The Zodiac", "Thriller")
        mem.store_film(fl)
        assert len(mem.filme) == 2

        fl = Film("2", "Star Wars", "Science Fiction")
        try:
            mem.store_film(fl)
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_delete_film():
        fl = Film("1", "Test", "Test")
        rep = RepositoryFilm()
        rep.store_film(fl)
        fl = Film("2", "Test", "Test")
        rep.store_film(fl)
        assert len(rep.filme) == 2
        rep.delete_film("1")
        assert len(rep.filme) == 1
        try:
            rep.delete_film("3")
            assert False
        except ValueError:
            assert True

    def teste_repository_filme(self):
        self.test_store_film()
        self.test_delete_film()
