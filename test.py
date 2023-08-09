from models.base import Base
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

print("coucou")
