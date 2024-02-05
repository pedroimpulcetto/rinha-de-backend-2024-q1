from fastapi import APIRouter, Depends, Query
from pydantic import PositiveInt

from app.api.dto.input.transaction import TransactionIn
from app.api.dto.output.statement import StatementOut
from app.api.dto.output.transaction import TransactionOut
from app.core.domain.usecase.create_transaction import CreateTransaction
from app.core.infra.db.client import ClientDatabase
from app.database import SessionLocal, get_db


"""
Transações
Requisição

POST /clientes/[id]/transacoes

{
    "valor": 1000,
    "tipo" : "c",
    "descricao" : "descricao"
}
Onde

[id] (na URL) deve ser um número inteiro representando a identificação do cliente.
valor deve um número inteiro positivo que representa centavos (não vamos trabalhar com frações de centavos). Por exemplo, R$ 10 são 1000 centavos.
tipo deve ser apenas c para crédito ou d para débito.
descricao deve ser uma string de 1 a 10 caractéres.
Todos os campos são obrigatórios.

Resposta

HTTP 200 OK

{
    "limite" : 100000,
    "saldo" : -9098
}
Onde

limite deve ser o limite cadastrado do cliente.
saldo deve ser o novo saldo após a conclusão da transação.
Obrigatoriamente, o http status code de requisições para transações bem sucedidas deve ser 200!

Regras Uma transação de débito nunca pode deixar o saldo do cliente menor que seu limite disponível. Por exemplo, um cliente com limite de 1000 (R$ 10) nunca deverá ter o saldo menor que -1000 (R$ -10). Nesse caso, um saldo de -1001 ou menor significa inconsistência na Rinha de Backend!

Se uma requisição para débito for deixar o saldo inconsistente, a API deve retornar HTTP Status Code 422 sem completar a transação! O corpo da resposta nesse caso não será testado e você pode escolher como o representar.

Se o atributo [id] da URL for de uma identificação não existe de cliente, a API deve retornar HTTP Status Code 404. O corpo da resposta nesse caso não será testado e você pode escolher como o representar. Se a API retornar algo como HTTP 200 informando que o cliente não foi encontrado no corpo da resposta ou HTTP 204 sem corpo, ficarei extremamente deprimido e a Rinha será cancelada para sempre.


"""

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"],
)

@router.post("/{id}/transacoes")
async def create_transaction(
    transaction: TransactionIn,
    client_id: PositiveInt = Query(alias='id', description="id do cliente"),
    db: SessionLocal = Depends(get_db)
):
    client_db = ClientDatabase(db)
    
    usecase = CreateTransaction(client_db)
    result = usecase.execute(client_id, transaction)
    return TransactionOut(limite=result['limite'], saldo=result['saldo'])


"""
Extrato
Requisição

GET /clientes/[id]/extrato

Onde

[id] (na URL) deve ser um número inteiro representando a identificação do cliente.
Resposta

HTTP 200 OK

{
  "saldo": {
    "total": -9098,
    "data_extrato": "2024-01-17T02:34:41.217753Z",
    "limite": 100000
  },
  "ultimas_transacoes": [
    {
      "valor": 10,
      "tipo": "c",
      "descricao": "descricao",
      "realizada_em": "2024-01-17T02:34:38.543030Z"
    },
    {
      "valor": 90000,
      "tipo": "d",
      "descricao": "descricao",
      "realizada_em": "2024-01-17T02:34:38.543030Z"
    }
  ]
}
Onde

saldo
total deve ser o saldo total atual do cliente (não apenas das últimas transações seguintes exibidas).
data_extrato deve ser a data/hora da consulta do extrato.
limite deve ser o limite cadastrado do cliente.
ultimas_transacoes é uma lista ordenada por data/hora das transações de forma decrescente contendo até as 10 últimas transações com o seguinte:
valor deve ser o valor da transação.
tipo deve ser c para crédito e d para débito.
descricao deve ser a descrição informada durante a transação.
realizada_em deve ser a data/hora da realização da transação.
Regras Se o atributo [id] da URL for de uma identificação não existente de cliente, a API deve retornar HTTP Status Code 404. O corpo da resposta nesse caso não será testado e você pode escolher como o representar. Já sabe o que acontece se sua API retornar algo na faixa 2XX, né? Agradecido.
"""

@router.get("/{id}/extrato")
async def get_statement(id: int):
    return StatementOut(
        saldo={
            "total": -9098,
            "data_extrato": "2024-01-17T02:34:41.217753Z",
            "limite": 100000
        },
        ultimas_transacoes=[
            {
                "valor": 10,
                "tipo": "c",
                "descricao": "descricao",
                "realizada_em": "2024-01-17T02:34:38.543030Z"
            },
            {
                "valor": 90000,
                "tipo": "d",
                "descricao": "descricao",
                "realizada_em": "2024-01-17T02:34:38.543030Z"
            }
        ]
    )