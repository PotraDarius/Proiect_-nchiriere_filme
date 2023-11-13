from Validator.validator_client_module import ValidatorClient
from Validator.validator_film_module import ValidatorFilm
from Repository.repository_client_module import RepositoryClient
from Repository.repository_film_module import RepositoryFilm
from Service.service_client_module import ServiceClient

# creare validatori
validator_client = ValidatorClient()
validator_film = ValidatorFilm()

# creare repositories
repo_client = RepositoryClient()
repo_film = RepositoryFilm()

# creare servicii
sv_client = ServiceClient(repo_client,validator_client)
