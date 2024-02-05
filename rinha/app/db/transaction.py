from sqlalchemy import INTEGER, Column, ForeignKey, String
from app.database import Base


class Transaction(Base):
        __tablename__ = 'transacoes'
    
        id = Column(INTEGER, primary_key=True)
        client_id = Column(INTEGER, ForeignKey('clientes.id'))
        valor = Column(INTEGER)
        tipo = Column(String(1))
        descricao = Column(String(255))