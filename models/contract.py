from models.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    remaining_to_pay = Column(Float)
    create_date = Column(Date)
    status = Column(String(255))

    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="contracts")

    def __repr__(self):
        return f'Contrat {self.id}'
