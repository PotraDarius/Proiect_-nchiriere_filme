from Validator.validator_client_module import ValidatorClient
from Validator.validator_film_module import ValidatorFilm
from Validator.validator_UI_module import ValidatorUI
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
from Service.service_client_module import ServiceClient
from Service.service_film_module import ServiceFilm
from UI.UI_module import UI
from Teste.teste_module import Tester

# creare validatori
validator_client = ValidatorClient()
validator_film = ValidatorFilm()
validator_UI = ValidatorUI()

# creare repositories
repo_client = RepositoryClient()
repo_film = RepositoryFilm()

# creare servicii
sv_client = ServiceClient(repo_client, validator_client)
sv_film = ServiceFilm(repo_film, repo_client, validator_film)

# creare UI
ui = UI(sv_client, sv_film, validator_UI)

# rulare teste
tester = Tester()
tester.ruleaza_teste()

sv_client.load_from_file_to_repository_client()
sv_film.load_from_file_to_repository_film()

ui.meniu_principal()

sv_client.load_from_repository_client_to_file()
sv_film.load_from_repository_film_to_file()
