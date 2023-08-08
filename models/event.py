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

    support_id = Column(Integer, ForeignKey('collaborator.id'))
    support = relationship("Collaborator", back_populates="events")

    contract_id = Column(Integer, ForeignKey('contract.id'))
    contract = relationship("Contract", back_populates="event")

    def __repr__(self):
        return f'{self.title}'
