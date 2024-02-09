from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from app.api.dto.input.transaction import TransactionIn
from app.core.domain.repository.client import ClientRepository

from app.db.client import Client
from app.db.transaction import Transaction


class ClientDatabase(ClientRepository):
    def __init__(self, conn: Session) -> None:
        self.conn = conn

    def get_client(self, client_id: int) -> Client:
        return self.conn.query(Client).filter(Client.id == client_id).first()
    
    def update_client(self, client: Client) -> None:
        # self.conn.add(client)
        self.conn.commit()
        self.conn.refresh(client)

    def save_transaction(self, client_id: int, transaction: TransactionIn) -> None:
        new_transaction = Transaction(
            cliente_id=client_id,
            valor=transaction.amount,
            tipo=transaction.type.value,
            descricao=transaction.description,
            data=datetime.utcnow()
        )
        self.conn.add(new_transaction)
        self.conn.commit()
        self.conn.refresh(new_transaction)

    def get_statement_by_client_id(self, client_id: int) -> list:
        # make only one query to get client data and last 10 transactions
        client = self.conn.query(Client).filter(Client.id == client_id).first()
        return client