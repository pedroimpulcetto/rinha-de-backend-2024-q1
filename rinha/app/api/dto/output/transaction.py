from pydantic import BaseModel, Field

class TransactionOut(BaseModel):
    limit: int = Field(..., alias="limite")
    balance: int = Field(..., alias="saldo")