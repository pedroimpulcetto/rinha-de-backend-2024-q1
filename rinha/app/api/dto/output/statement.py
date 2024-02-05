from datetime import datetime
from pydantic import BaseModel, Field

class StatementTransactionOut(BaseModel):
    amount: int = Field(..., alias="valor")
    type: str = Field(..., alias="tipo")
    description: str = Field(..., alias="descricao")
    created_at: str = Field(..., alias="realizada_em")


class StatementBalanceOut(BaseModel):
    total: int = Field(..., alias="total")
    date: str = Field(..., alias="data_extrato", default_factory=datetime.now().isoformat)
    limit: int = Field(..., alias="limite")


class StatementOut(BaseModel):
    balance: StatementBalanceOut = Field(..., alias="saldo")
    last_transactions: list[StatementTransactionOut] = Field(..., alias="ultimas_transacoes")