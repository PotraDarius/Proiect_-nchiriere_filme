from Domain.client_module import test_creare_client
from Domain.film_module import test_creare_film
from Repository.repository_client_module import teste_repository_client
from Repository.repository_film_module import teste_repository_filme
from Service.service_client_module import teste_service_client
from Service.service_film_module import teste_serice_filme
from Validator.validator_film_module import teste_validator_film
from Validator.validator_client_module import teste_validator_client
from Validator.validator_UI_module import test_validare_optiune

def teste():
    test_creare_client()
    test_creare_film()
    teste_repository_client()
    teste_repository_filme()
    teste_service_client()
    teste_serice_filme()
    teste_validator_client()
    teste_validator_film()
    test_validare_optiune()


teste()
