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

    def alegere_optiune(self):
        p = input("Dati o optiune: ")
        self.validator.validare_optiune(p)
        return int(p)

    def meniu_adaugare(self):
        while True:
            print("1.Adauga client")
            print("2.Adauga film")
            print("3.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                id = int(input("Dati id-ul: "))
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
            if p == 1:
                id = int(input("Dati id-ul: "))
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
            if p == 1:
                id = int(input("Dati id-ul clientului: "))
                nume = input("Dati noua valoare a numelui: ")
                self.service_client.modificare_client(p, id, nume)
                print("Modificare reusita!")
            elif p == 2:
                id = int(input("Dati id-ul clientului: "))
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
            if p == 1:
                id = input("Dati id-ul filmului: ")
                titlu = input("Dati noua valoare a titlului: ")
                self.service_film.modifica_film(p, id, titlu)
                print("Modificare reusita!")
            elif p == 2:
                id = input("Dati id-ul filmului: ")
                gen = input("Dati noua valoare a genului: ")
                self.service_film.modifica_film(p, id, gen)
                print("Modificare reusita!")
            elif p == 3:
                break

    def meniu_modificare(self):
        while True:
            print("1.Modificare client")
            print("2.Modificare film")
            print("3.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                self.meniu_modificare_client()
            elif p == 2:
                self.meniu_modificare_film()
            elif p == 3:
                break

    def meniu_cautare_clienti(self):
        while True:
            print("1.Cautare clienti dupa nume")
            print("2.Cautare clienti dupa prenume")
            print("3.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                nume = input("Dati numele dupa care vreti sa cautati clienti: ")
                dict = self.service_client.cautare_clienti_dupa_nume(nume)
                if dict == {}:
                    print("Nu s-a gasit niciun client cu acest nume!")
                else:
                    self.service_client.afisare_rezultat_cautare_clienti(dict)
            elif p == 2:
                prenume = input("Dati prenumele dupa care vreti sa cautati clienti: ")
                dict = self.service_client.cautare_clienti_dupa_prenume(prenume)
                if dict == {}:
                    print("Nu s-a gasit niciun client cu acest prenume!")
                else:
                    self.service_client.afisare_rezultat_cautare_clienti(dict)
            elif p == 3:
                break

    def meniu_cautare_filme(self):
        while True:
            print("1.Cautare dupa titlu")
            print("2.Cautare dupa gen")
            print("3.Cautare dupa filme de inchiriat")
            print("4.Cautare dupa filme inchiriate")
            print("5.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                titlu = input("Dati titlul dupa care vreti sa cautati filme: ")
                dict = self.service_film.cautare_filme_dupa_titlu(titlu)
                if dict == {}:
                    print("Nu s-a gasit un film cu titlul dat!")
                else:
                    self.service_film.afisare_rezultat_cautare_filme(dict)
            elif p == 2:
                gen = input("Dati genul dupa care vreti sa cautati filme: ")
                dict = self.service_film.cautare_filme_dupa_gen(gen)
                if dict == {}:
                    print("Nu s-a gasit un film cu genul dat!")
                else:
                    self.service_film.afisare_rezultat_cautare_filme(dict)
            elif p == 3:
                dict = self.service_film.cautare_filme_de_inchiriat()
                if dict == {}:
                    print("Toate filmele sunt inchiriate!")
                else:
                    self.service_film.afisare_rezultat_cautare_filme(dict)
            elif p == 4:
                dict = self.service_film.cautare_filme_inchiriate()
                if dict == {}:
                    print("Nu exista film ce este inchiriat!")
                else:
                    self.service_film.afisare_rezultat_cautare_filme(dict)
            elif p == 5:
                break

    def meniu_inchiriere(self):
        id_client = int(input("Dati id-ul clientului ce va inchiria filmul: "))
        id = input("Dati id-ul filmului ce doriti sa il inchiriati: ")
        self.service_film.inchiriere_film(id, id_client)
        print("Inchiriere reusita!")

    def meniu_returnare(self):
        id = input("Dati id-ul filmului ce doriti sa il returnati: ")
        self.service_film.returnare_film(id)
        print("Returnare reusita!")

    def meniu_rapoarte(self):
        while True:
            print("1.Afisare clienti cu filme inchiriate ordonati dupa nume")
            print("2.Afisare clienti cu filme inchiriate ordonati dupa numarul de filme inchiriate")
            print("3.Afisare cele mai inchiriate filme")
            print("4.Afisare primii 30% clienti cu cele mai multe filme inchiriate")
            print("5.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                dict = self.service_client.ordonare_clienti_dupa_nume()
                if dict == {}:
                    print("Lista de clienti este goala!")
                else:
                    self.service_client.afisare_rezultat_rapoarte_clienti(dict)
            elif p == 2:
                dict = self.service_client.ordonare_clienti_dupa_nr_filme_inchiriate()
                if dict == {}:
                    print("Lista de clienti este goala!")
                else:
                    self.service_client.afisare_rezultat_rapoarte_clienti(dict)
            elif p == 3:
                dict = self.service_film.cele_mai_inchiriate_filme()
                if dict == {}:
                    print("Lista de filme este goala!")
                self.service_film.afisare_cele_mai_inchiriate_filme(dict)
            elif p == 4:
                dict = self.service_client.primii_30lasuta_clienti_cu_filme_inchiriate()
                if dict == {}:
                    print("Lista de filme este goala!")
                self.service_client.afisare_rezultat_rapoarte_clienti(dict)
            elif p == 5:
                break

    def meniu_generare_random(self):
        while True:
            print("1.Generare clienti")
            print("2.Generare filme")
            print("3.Inapoi")
            p = self.alegere_optiune()
            if p == 1:
                x = int(input("Dati numarul de clienti doriti: "))
                self.validator.validare_optiune(x)
                self.service_client.generare_random_clienti(x)
                print("Generare reusita!")
            elif p == 2:
                x = int(input("Dati numarul de filme dorite: "))
                self.validator.validare_optiune(x)
                self.service_film.generare_random_filme(x)
                print("Generare reusita!")
            elif p == 3:
                break

    def meniu_principal(self):
        while True:
            print("Meniul aplicatiei")
            print("1.Adauga film/client")
            print("2.Sterge film/client")
            print("3.Modifica film/client")
            print("4.Afisare lista clienti")
            print("5.Afisare lista filme")
            print("6.Cautare clienti")
            print("7.Cautare filme")
            print("8.Inchiriere film")
            print("9.Returnare film")
            print("10.Rapoarte")
            print("11.Generare random de filme")
            print("12.Iesire")
            p = self.alegere_optiune()

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
                self.meniu_cautare_clienti()
            elif p == 7:
                self.meniu_cautare_filme()
            elif p == 8:
                self.meniu_inchiriere()
            elif p == 9:
                self.meniu_returnare()
            elif p == 10:
                self.meniu_rapoarte()
            elif p == 11:
                self.meniu_generare_random()
            elif p == 12:
                break
