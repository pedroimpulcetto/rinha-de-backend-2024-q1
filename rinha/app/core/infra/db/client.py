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
        self.conn.add(client)
        self.conn.commit()
        self.conn.refresh(client)