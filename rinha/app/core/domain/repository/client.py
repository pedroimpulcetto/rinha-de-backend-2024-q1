from abc import ABC, abstractmethod

from httpx import Client

class ClientRepository(ABC):

    @abstractmethod
    def get_client(self, client_id: int) -> Client:
        pass
    
    @abstractmethod
    def update_client(self, client: Client) -> None:
        pass