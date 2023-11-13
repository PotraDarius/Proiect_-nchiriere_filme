
class UI:
    """
    Clasa ce va defini o interfata

    """
    def __init__(self, sv_client, sv_film, validator_UI):
        self.service_client = sv_client
        self.service_film = sv_film
        self.validator = validator_UI
        self.UI_client = 0
        self.UI_film = 0

    @staticmethod
    def alegere_optiune():
        return input("Dati o optiune: ")

    def meniu_adaugare(self):
        while True:
            print("1.Adauga client")
            print("2.Adauga film")
            print("3.Inapoi")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            if p == 1:
                id = input("Dati id-ul: ")
                nume = input("Dati numele: ")
                prenume = input("Dati prenumele: ")
                self.service_client.add_client(id, nume, prenume)
                print("Adauagre reusita!")
            elif p == 2:
                id = input("Dati id-ul: ")
                titlu = input("Dati titlul: ")
                gen = input("Dati genul: ")
                self.service_film.add_film(id, titlu, gen)
                print("Adaugare reusita!")
            elif p == 3:
                break

    def meniu_stergere(self):
        while True:
            print("1.Sterge client")
            print("2.Sterge film")
            print("3.Inapoi")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            if p == 1:
                id = input("Dati id-ul: ")
                self.service_client.stergere_client(id)
                print("Stergere reusita!")
            elif p == 2:
                id = input("Dati id-ul: ")
                self.service_film.stergere_film(id)
                print("Stergere reusita!")
            elif p == 3:
                break

    def meniu_modificare_client(self):
        while True:
            print("1.Modificare nume")
            print("2.Modificare prenume")
            print("3.Inapoi")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            id = input("Dati id-ul clientului: ")
            if p == 1:
                nume = input("Dati noua valoare a numelui: ")
                self.service_client.modificare_client(p, id, nume)
                print("Modificare reusita!")
            elif p == 2:
                prenume = input("Dati noua valoare a prenumelui: ")
                self.service_client.modificare_client(p, id, prenume)
                print("Modificare reusita!")
            elif p == 3:
                break

    def meniu_modificare_film(self):
        while True:
            print("1.Modificare titlu")
            print("2.Modificare gen")
            print("3.Inapoi")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            id = input("Dati id-ul filmului: ")
            if p == 1:
                titlu = input("Dati noua valoare a titlului: ")
                self.service_film.modificare_film(p, id, titlu)
                print("Modificare reusita!")
            elif p == 2:
                gen = input("Dati noua valoare a genului: ")
                self.service_film.modificare_film(p, id, gen)
                print("Modificare reusita!")
            elif p == 3:
                break

    def meniu_modificare(self):
        while True:
            print("1.Modificare client")
            print("2.Modificare film")
            print("3.Inapoi")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            if p == 1:
                self.meniu_modificare_client()
            elif p == 2:
                self.meniu_modificare_film()
            elif p == 3:
                pass

    def meniu_principal(self):
        while True:
            print("Meniul aplicatiei")
            print("1.Adauga film/client")
            print("2.Sterge film/client")
            print("3.Modifica film/client")
            print("4.Afisare lista clienti")
            print("5.Afisare lista filme")
            print("6.Iesire")
            p = self.alegere_optiune()
            self.validator.validare_optiune(p)
            p = int(p)
            if p == 1:
                self.meniu_adaugare()
            elif p == 2:
                self.meniu_stergere()
            elif p == 3:
                self.meniu_modificare()
            elif p == 4:
                self.service_client.afisare_lista_clienti()
            elif p == 5:
                self.service_film.afisare_lista_filme()
            elif p == 6:
                break
