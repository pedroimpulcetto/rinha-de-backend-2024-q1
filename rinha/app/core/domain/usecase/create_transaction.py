

from app.api.dto.input.transaction import TransactionIn, TransactionTypeIn
from app.core.domain.entity.client import ClientEntity
from app.core.infra.db.client import ClientDatabase

"""
Regras Uma transação de débito nunca pode deixar o saldo do cliente menor que seu limite disponível. Por exemplo, um cliente com limite de 1000 (R$ 10) nunca deverá ter o saldo menor que -1000 (R$ -10). Nesse caso, um saldo de -1001 ou menor significa inconsistência na Rinha de Backend!

Se uma requisição para débito for deixar o saldo inconsistente, a API deve retornar HTTP Status Code 422 sem completar a transação! O corpo da resposta nesse caso não será testado e você pode escolher como o representar.
"""

class CreateTransaction:
    def __init__(self, client_db: ClientDatabase):
        self.client_db = client_db

    def execute(self, client_id: int, transaction: TransactionIn):
        client = self.client_db.get_client(client_id)
        if not client:
            raise ValueError("Client not found")
      
        if transaction.type == TransactionTypeIn.DEBIT and client.saldo - transaction.amount < -client.limite:
            raise ValueError("Insufficient funds")
        
        client.saldo += transaction.amount if transaction.type == TransactionTypeIn.CREDIT else -transaction.amount
        self.client_db.update_client(client)
        return {"limite": client.limite, "saldo": client.saldo}
        