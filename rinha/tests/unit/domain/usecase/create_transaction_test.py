

from app.api.dto.input.transaction import TransactionIn
from app.core.domain.usecase.create_transaction import CreateTransaction
from pytest import raises


def test_should_create_transaction_with_correct_values(mock_client_repository):
    fake_transaction = TransactionIn(valor=100, tipo='d', descricao='Teste')
    usecase = CreateTransaction(mock_client_repository)
    result = usecase.execute(1, fake_transaction)
    mock_client_repository.get_client.assert_called_once_with(1)
    mock_client_repository.update_client.assert_called_once()
    assert result['saldo'] == -900
    assert result['limite'] == 1000



def test_should_not_create_transaction_when_client_has_no_saldo(mock_client_repository):
    fake_transaction = TransactionIn(valor=1001, tipo='d', descricao='Teste')
    usecase = CreateTransaction(mock_client_repository)
    with raises(ValueError) as exc:
        usecase.execute(1, fake_transaction)
        assert str(exc.value) == "Insufficient funds"
        
    mock_client_repository.get_client.assert_called_once_with(1)


