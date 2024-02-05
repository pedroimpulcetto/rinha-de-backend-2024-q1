from sqlalchemy import INTEGER, Column, String
from app.database import Base


class Client(Base):

    __tablename__ = 'clientes'

    id = Column(INTEGER, primary_key=True)
    nome = Column(String(255))
    limite = Column(INTEGER)
    saldo = Column(INTEGER, nullable=True)