from models.person import Person, UniqueEmailMixin
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func


class Client(Person, UniqueEmailMixin):
    __tablename__ = 'client'

    enterprise_name = Column(String(255))
    # create_date = Column(Date, server_default=func.current_date())
    create_date = Column(Date)
    last_update_date = Column(Date)
    # Relationship with Collaborator (commercial contact for the client)
    contact_id = Column(Integer, ForeignKey('collaborator.id', ondelete="SET NULL"))
    contact = relationship("Collaborator", back_populates="clients")
    # Relationship with Contract (contracts linked to the client)
    contracts = relationship("Contract", back_populates="client")
