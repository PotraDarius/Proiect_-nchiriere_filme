from Teste.tester_client_module import TesterClient
from Teste.tester_film_module import TesterFilm
from Teste.tester_inchiriere_returnare_module import TesterInchiriereReturnare

from Teste.tester_repository_client_module import TesterRepoClient
from Teste.tester_repository_film_module import TesterRepoFilm
from Teste.tester_repository_inchiriere_returnare_module import TesterRepoInchiriereReturnare

from Teste.tester_service_client_module import TesterServiceClient
from Teste.tester_service_film_module import TesterServiceFilm
from Teste.tester_service_inchiriere_returnare_module import TesterServiceInchiriereReturnare

from Teste.tester_validator_client_module import TesterValidatorClient
from Teste.tester_validator_film_module import TesterValidatorFilm
from Teste.tester_validator_UI_module import TesterValidatorUI
from Teste.tester_validator_inchiriere_returnare_module import TesterValidatorInchiriereReturnare

class Tester:
    """
    Clasa ce se ocupa cu toate testele din aplicatie
    """
    def __init__(self):
        self.tester_client = TesterClient()
        self.tester_film = TesterFilm()
        self.tester_inchiriere_returnare = TesterInchiriereReturnare()

        self.tester_repo_client = TesterRepoClient()
        self.tester_repo_film = TesterRepoFilm()
        self.tester_repo_inchiriere_returnare = TesterRepoInchiriereReturnare()

        self.tester_validator_client = TesterValidatorClient()
        self.tester_validator_film = TesterValidatorFilm()
        self.tester_validator_UI = TesterValidatorUI()
        self.tester_validator_inchiriere_returnare = TesterValidatorInchiriereReturnare()

        self.tester_service_client = TesterServiceClient()
        self.tester_service_film = TesterServiceFilm()
        self.tester_service_inchiriere_returnare = TesterServiceInchiriereReturnare()

    def ruleaza_teste(self):
        self.tester_client.test_creare_client()
        self.tester_film.test_creare_film()
        self.tester_inchiriere_returnare.test_inchiriere_returnare()

        self.tester_repo_client.teste_repository_client()
        self.tester_repo_film.teste_repository_filme()
        self.tester_repo_inchiriere_returnare.teste_repo_inchiriere_returnare()

        self.tester_validator_client.teste_validator_client()
        self.tester_validator_film.teste_validator_film()
        self.tester_validator_UI.test_validare_optiune()
        self.tester_validator_inchiriere_returnare.teste_validator_inchiriere_returnare()

        self.tester_service_client.teste_service_client()
        self.tester_service_film.teste_serice_filme()
        self.tester_service_inchiriere_returnare.teste_service_inchiriere_returnare()
