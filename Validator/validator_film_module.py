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

    @classmethod
    def validare_modificator(cls, modificator):
        if modificator == "":
            raise ValueError("Noua valoare nu poate fi goala!")
