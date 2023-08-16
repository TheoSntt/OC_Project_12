from models.person import Person, UniqueEmailMixin
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Collaborator(Person, UniqueEmailMixin):
    __tablename__ = 'collaborator'
    username = Column(String(255))
    password = Column(String(255))
    # Relationship with Client (clients for whom the collaborator is commercial contact)
    clients = relationship("Client", back_populates="contact")
    # Relationship with Event (events for which the collaborator is support)
    events = relationship("Event", back_populates="support")
    # role = Column(Enum("administrator", "sales", "support"))
    role_id = Column(Integer, ForeignKey('role.id', ondelete="SET NULL"))
    role = relationship("Role", back_populates="collaborators")
