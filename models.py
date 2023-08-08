from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Person(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255))
    telephone = Column(Integer)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Client(Person):
    __tablename__ = 'client'

    enterprise_name = Column(String(255))
    create_date = Column(Date)
    last_update_date = Column(Date)

    contact_id = Column(Integer, ForeignKey('collaborator.id'))
    contact = relationship("Collaborator", back_populates="clients")


class Collaborator(Person):
    __tablename__ = 'collaborator'

    # role = Column(String(255))
    role = Column(Enum("administrator", "sales", "support"))


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
