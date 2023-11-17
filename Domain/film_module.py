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

    def get_inchiriat(self):
        return self.__inchiriat

    def set_inchiriat(self, bool_value):
        self.__inchiriat = bool_value

    def set_nr_inchirieri(self, nr):
        self.__nr_inchirieri = nr

    def get_nr_inchirieri(self):
        return self.__nr_inchirieri

    def creste_nr_inchirieri(self):
        self.__nr_inchirieri += 1
