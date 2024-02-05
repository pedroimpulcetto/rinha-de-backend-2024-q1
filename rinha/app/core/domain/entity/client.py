

from pydantic import BaseModel


class ClientEntity(BaseModel):
    name: str
    amount: int
    limit: int
    balance: int

    def amount_to_real(self):
        return self.amount / 100