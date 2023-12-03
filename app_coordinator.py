from Validator.validator_client_module import ValidatorClient
from Validator.validator_film_module import ValidatorFilm
from Validator.validator_UI_module import ValidatorUI
from Validator.validator_inchiriere_returnare_module import ValidatorInchiriereReturnare
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
from Repository.repository_inchiriere_returnare_module import RepositoryInchiriereReturnare
from Service.service_client_module import ServiceClient
from Service.service_film_module import ServiceFilm
from Service.service_inchiriere_returnare_module import ServiceInchirereReturnare
from UI.UI_module import UI
from Teste.teste_module import Tester


# creare repositories
repo_client = RepositoryClient()
repo_film = RepositoryFilm()
repo_inchirieri_returnari = RepositoryInchiriereReturnare()

# creare validatori
validator_client = ValidatorClient()
validator_film = ValidatorFilm()
validator_UI = ValidatorUI()
validator_inchiriere_returnare = ValidatorInchiriereReturnare(repo_client, repo_film, repo_inchirieri_returnari)

# creare servicii
sv_client = ServiceClient(repo_client, validator_client)
sv_film = ServiceFilm(repo_film, repo_client, repo_inchirieri_returnari, validator_film)
sv_inchirieri_returnari = ServiceInchirereReturnare(repo_inchirieri_returnari, validator_inchiriere_returnare,
                                                    repo_client, repo_film)

# creare UI
ui = UI(sv_client, sv_film, sv_inchirieri_returnari, validator_UI)

# rulare teste
tester = Tester()
tester.ruleaza_teste()

p = ui.alegere_stocare_date()

if p == 2:
    sv_client.load_from_file_to_repository_client()
    sv_film.load_from_file_to_repository_film()
    sv_inchirieri_returnari.load_from_file_to_repository_inchirieri()

ui.meniu_principal()

if p == 2:
    sv_client.load_from_repository_client_to_file()
    sv_film.load_from_repository_film_to_file()
    sv_inchirieri_returnari.load_from_repository_inchirieri_to_file()
