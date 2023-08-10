from models.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    remaining_to_pay = Column(Float)
    create_date = Column(Date, server_default=func.now().date())
    status = Column(String(255))
    # Relationship with Client (client to whom the contract is linked)
    client_id = Column(Integer, ForeignKey('client.id', ondelete="SET NULL"))
    client = relationship("Client", back_populates="contracts")
    # Relationship with Event (event to which the contract is linked)
    event = relationship("Event", back_populates="contract")

    def __repr__(self):
        return f'Contrat {self.id}'
