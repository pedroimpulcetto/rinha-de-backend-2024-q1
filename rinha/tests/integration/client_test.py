from fastapi.testclient import TestClient

def test_should_create_credit_transaction(build_client: TestClient) -> None:
    client_id = 1
    transaction = {
        "valor": 10,
        "tipo": "c",
        "descricao": "descricao"
    }
    response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    assert response.status_code == 200
    assert response.json() == {
        "limite": 100000,
        "saldo": 10
    }

def test_should_create_debit_transaction(build_client: TestClient) -> None:
    client_id = 1
    transaction = {
        "valor": 100,
        "tipo": "d",
        "descricao": "descricao"
    }
    response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    assert response.status_code == 200
    assert response.json() == {
        "limite": 100000,
        "saldo": -100
    }

def test_should_not_create_debit_transaction(build_client: TestClient) -> None:
    client_id = 1
    transaction = {
        "valor": 100001,
        "tipo": "d",
        "descricao": "descricao"
    }
    response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    assert response.status_code == 422


def test_should_not_create_debit_transaction_no_user(build_client: TestClient) -> None:
    client_id = 10
    transaction = {
        "valor": 100001,
        "tipo": "d",
        "descricao": "descricao"
    }
    response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    assert response.status_code == 404

def test_should_list_statement(build_client: TestClient) -> None:
    client_id = 1
    transaction = {
        "valor": 100,
        "tipo": "d",
        "descricao": "descricao"
    }
    # response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    # response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    # response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    # response = build_client.post(f"/clientes/{client_id}/transacoes", json=transaction)
    response = build_client.get(f"/clientes/{client_id}/extrato")
    assert response.status_code == 200