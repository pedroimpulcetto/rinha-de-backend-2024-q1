from enum import Enum
from pydantic import BaseModel, PositiveInt, Field

class TransactionTypeIn(Enum):
    CREDIT = "c"
    DEBIT = "d"


class TransactionIn(BaseModel):
    amount: PositiveInt = Field(..., alias="valor")
    type: TransactionTypeIn = Field(..., alias="tipo")
    description: str = Field(..., alias="descricao", max_length=10, min_length=1)