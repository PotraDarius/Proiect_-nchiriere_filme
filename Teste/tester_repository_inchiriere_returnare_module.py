from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Domain.inchiriere_returnare_module import InchiriereReturnare
class TesterRepoInchiriereReturnare:

    @staticmethod
    def test_add_inchiriere():
        inchiriere = InchiriereReturnare(2, "3")
        rep = RepositoryInchiriereReturnare()
        rep.store_inchiriere(inchiriere)
        assert len(rep.inchirieri) == 1

    @staticmethod
    def test_delete_inchiriere():
        inchiriere = InchiriereReturnare(2, "3")
        inchiriere2 = InchiriereReturnare(3, "4")
        inchiriere3 = InchiriereReturnare(5, "6")
        rep = RepositoryInchiriereReturnare()
        rep.store_inchiriere(inchiriere)
        rep.store_inchiriere(inchiriere2)
        assert len(rep.inchirieri) == 2
        rep.delete_inchiriere(inchiriere)
        assert len(rep.inchirieri) == 1
        rep.delete_inchiriere(inchiriere3)
        assert len(rep.inchirieri) == 1

    @staticmethod
    def test_verificare_status_film():
        inchiriere = InchiriereReturnare(2, "3")
        rep = RepositoryInchiriereReturnare()
        rep.store_inchiriere(inchiriere)

        assert rep.verificare_status_film("3") is True
        assert rep.verificare_status_film("4") is False

    def teste_repo_inchiriere_returnare(self):
        self.test_add_inchiriere()
        self.test_delete_inchiriere()
        self.test_verificare_status_film()
