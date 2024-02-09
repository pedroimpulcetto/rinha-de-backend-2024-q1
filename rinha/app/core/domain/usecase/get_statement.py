




from app.api.dto.output.statement import StatementBalanceOut, StatementOut, StatementTransactionOut
from app.core.infra.db.client import ClientDatabase
from datetime import datetime


class GetStatement():
    def __init__(self, client_db: ClientDatabase):
        self.client_db = client_db

    def execute(self, client_id: int) -> dict:
        client = self.client_db.get_statement_by_client_id(client_id)
        if not client:
            raise ValueError("Client not found")
        
        balance = StatementBalanceOut(
            total=client.saldo,
            limite=client.limite,
        )

        client_transactions = []
        for transaction in client.transacoes:
            client_transaction = StatementTransactionOut(
                valor=transaction.valor,
                tipo=transaction.tipo,
                descricao=transaction.descricao,
                realizada_em=transaction.data.isoformat()
            )
            client_transactions.append(client_transaction)
        
        return StatementOut(
            saldo=balance,
            ultimas_transacoes=client_transactions
        )