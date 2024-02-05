
from pytest import fixture

from app.core.domain.repository.client import ClientRepository
from app.db.client import Client

@fixture
def mock_client_repository(mocker):
    repository = mocker.Mock(ClientRepository)
    repository.get_client.return_value = Client(id=1, nome='Teste', limite=1000, saldo=-800)
    return repository