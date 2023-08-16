from models.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    legal_id = Column(String(255), unique=True, nullable=False)
    price = Column(Float)
    remaining_to_pay = Column(Float)
    # create_date = Column(Date, server_default=func.current_date())
    create_date = Column(Date)
    status = Column(String(255))
    # Relationship with Client (client to whom the contract is linked)
    client_id = Column(Integer, ForeignKey('client.id', ondelete="SET NULL"))
    client = relationship("Client", back_populates="contracts")
    # Relationship with Event (event to which the contract is linked)
    event = relationship("Event", back_populates="contract")

    __table_args__ = (
        UniqueConstraint('legal_id', name='uq_legalid'),
    )

    def __repr__(self):
        return f'Contrat {self.id}'
