from sqlalchemy import INTEGER, Column, String
from app.database import Base
from sqlalchemy.orm import relationship


class Client(Base):

    __tablename__ = 'clientes'

    id = Column(INTEGER, primary_key=True, index=True)
    nome = Column(String(255))
    limite = Column(INTEGER)
    saldo = Column(INTEGER, nullable=True)

    transacoes = relationship("Transaction", back_populates="cliente", lazy='joined')