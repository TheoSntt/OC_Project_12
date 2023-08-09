from models.person import Person
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship


class Collaborator(Person):
    __tablename__ = 'collaborator'

    role = Column(Enum("administrator", "sales", "support"))
    # Relationship with Client (clients for whom the collaborator is commercial contact)
    clients = relationship("Client", back_populates="contact")
    # Relationship with Event (events for which the collaborator is support)
    events = relationship("Event", back_populates="support")
