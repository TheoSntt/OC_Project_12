from models.person import Person
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Client(Person):
    __tablename__ = 'client'

    enterprise_name = Column(String(255))
    create_date = Column(Date)
    last_update_date = Column(Date)

    contact_id = Column(Integer, ForeignKey('collaborator.id'))
    contact = relationship("Collaborator", back_populates="clients")
