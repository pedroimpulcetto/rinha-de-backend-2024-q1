from sqlalchemy import INTEGER, TIMESTAMP, Column, ForeignKey, String, func
from app.database import Base
from sqlalchemy.orm import relationship


class Transaction(Base):
        __tablename__ = 'transacoes'
    
        id = Column(INTEGER, primary_key=True)
        cliente_id = Column(INTEGER, ForeignKey('clientes.id'))
        valor = Column(INTEGER)
        tipo = Column(String(1))
        descricao = Column(String(255))
        data = Column(TIMESTAMP, server_default=func.now())

        cliente = relationship("Client", back_populates="transacoes")