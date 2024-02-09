from abc import ABC, abstractmethod

from httpx import Client

from app.api.dto.input.transaction import TransactionIn

class ClientRepository(ABC):

    @abstractmethod
    def get_client(self, client_id: int) -> Client:
        pass
    
    @abstractmethod
    def update_client(self, client: Client) -> None:
        pass

    @abstractmethod
    def save_transaction(self, client_id: int, transaction: TransactionIn) -> None:
        pass

    @abstractmethod
    def get_statement_by_client_id(self, client_id: int) -> list:
        pass