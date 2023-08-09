from models.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)

    title = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    location = Column(String(1000))
    attendees = Column(Integer)
    comments = Column(String(1000))
    # Relationship with Collaborator (support in charge of the event)
    support_id = Column(Integer, ForeignKey('collaborator.id', ondelete="SET NULL"))
    support = relationship("Collaborator", back_populates="events")
    # Relationship with Contract (Contract for the event)
    contract_id = Column(Integer, ForeignKey('contract.id', ondelete="SET NULL"))
    contract = relationship("Contract", back_populates="event")

    def __repr__(self):
        return f'{self.title}'
