

from pydantic import BaseModel



class AccountEntity(BaseModel):
    limit: int
    balance: int

    def credit(self, value: int):
        self.balance += value

    def debit(self, value: int):
        if self.balance - value < -self.limit:
            raise ValueError("The value is greater than the limit")
        self.balance -= value


class ClientEntity(BaseModel):
    name: str
    account: AccountEntity
