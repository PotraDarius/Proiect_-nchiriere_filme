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

def test_creare_film():
    fl = Film("1", "Se7en", "Thriller")
    assert fl.get_id() == "1"
    assert fl.get_titlu() == "Se7en"
    assert fl.get_gen() == "Thriller"


test_creare_film()
