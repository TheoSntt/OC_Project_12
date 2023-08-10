
from models.base import Base
from database.db_session import engine
from models.client import Client
from models.collaborator import Collaborator
from models.contract import Contract
from models.event import Event
from database.db_session import session
from dao.client_dao import ClientDao
from dao.collaborator_dao import CollaboratorDao
from dao.contract_dao import ContractDao
from dao.event_dao import EventDao
from datetime import date


# Drop tables if model changed
# Collaborator.__table__.drop(engine)
# Client.__table__.drop(engine)
# Contract.__table__.drop(engine)
# Event.__table__.drop(engine)

# Create (or update) tables based on model definitions
# Base.metadata.create_all(engine)

# Empty the tables
session.query(Collaborator).delete()
session.query(Client).delete()
session.query(Contract).delete()
session.query(Event).delete()
session.commit()

# Instanciate DAOs
client_dao = ClientDao(session)
collaborator_dao = CollaboratorDao(session)
contract_dao = ContractDao(session)
event_dao = EventDao(session)

# Populate initial data
first_collaborator = Collaborator(
    name="Jean",
    surname="Bon",
    email="jean.bon@gmail.com",
    telephone="0612564321",
    role="sales")
collaborator_dao.create(first_collaborator)
# print(first_collaborator)
# print(first_collaborator.id)

second_collaborator = Collaborator(
    name="Jeanne",
    surname="Bon",
    email="jeanne.bon@gmail.com",
    telephone="0605102577",
    role="support")
collaborator_dao.create(second_collaborator)
# print(second_collaborator)
# print(second_collaborator.id)

first_client = Client(
    name="Jean-Michel",
    surname="Clientelle",
    email="jm-clientelle@wanadoo.fr",
    telephone="0607050401",
    enterprise_name="Bellevie",
    create_date=date(2022, 5, 15),
    last_update_date=date(2023, 8, 9),
    contact_id=first_collaborator.id)
client_dao.create(first_client)

first_contract = Contract(
    price=1240.25,
    remaining_to_pay=220.25,
    create_date=date(2023, 5, 1),
    status="En cours",
    client_id=first_client.id)
contract_dao.create(first_contract)

first_event = Event(
    title="Mariage super",
    start_date=date(2023, 9, 30),
    end_date=date(2023, 10, 2),
    location="Petaouchnok",
    attendees=234,
    comments="Ca va être chouette",
    support_id=second_collaborator.id,
    contract_id=first_contract.id)
event_dao.create(first_event)

first_event.location = "Petaouchnok-les-bains"
event_dao.update(first_event)