class Client:
    """
        Clasa ce reprezinta un client
        Domeniu: id - string
                 nume - string
                 prenume - string
                 lista_filme_inchriate - lista de filme
    """
    def __init__(self, id, nume, prenume):
        self.__id = id
        self.__nume = nume
        self.__prenume = prenume
        self.__lista_filme_inchiriate = []

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_prenume(self):
        return self.__prenume

    def set_nume(self, nume):
        self.__nume = nume

    def set_prenume(self, prenume):
        self.__prenume = prenume


class Film:
    """
        Clasa ce reprezinta un film
        Domeniu:
            id - string
            titlu - string
            gen - string
            nr_inchirieri - int
            inchiriat - bool


    """
    def __init__(self, id, titlu, gen):
        self.__id = id
        self.__titlu = titlu
        self.__gen = gen
        self.__nr_inchirieri = 0
        self.__inchiriat = False

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def get_gen(self):
        return self.__gen

    def set_gen(self, gen):
        self.__gen = gen

    def set_inchiriat(self, bool_value):
        self.__inchiriat = bool_value


class Validator:
    """
        Clasa ce se ocupa cu validarea datelor introduse
    """
    @classmethod
    def validare_client(cls, cl):
        """
            Validare client
            cl - Client
            raise ValueError
            if: id, nume sau prenume gol
        """
        erori = ""
        if cl.get_id() == "":
            erori += "Id-ul nu poate fi gol!"
        if cl.get_nume() == "":
            erori += "Numele nu poate fi gol!"
        if cl.get_prenume() == "":
            erori += "Prenumele nu poate fi gol!"
        if len(erori) > 0:
            raise ValueError(erori)

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


def test_creare_client():
    cl = Client("1", "Potra", "Darius")
    assert cl.get_id() == "1"
    assert cl.get_nume() == "Potra"
    assert cl.get_prenume() == "Darius"


def test_validare_client():
    cl = Client("", "Test", "Test")
    valid = Validator()
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


def test_creare_film():
    fl = Film("1", "Se7en", "Thriller")
    assert fl.get_id() == "1"
    assert fl.get_titlu() == "Se7en"
    assert fl.get_gen() == "Thriller"


def test_validare_film():
    fl = Film("1", "", "Test")
    valid = Validator()
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


def teste_domain():
    test_creare_client()
    test_validare_client()
    test_creare_film()
    test_validare_film()


teste_domain()
