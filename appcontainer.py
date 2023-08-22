from database.db_session import session
from dao.client_dao import ClientDao
from dao.collaborator_dao import CollaboratorDao
from dao.contract_dao import ContractDao
from dao.event_dao import EventDao
from repository.client_repository import ClientRepository
from repository.collaborator_repository import CollaboratorRepository
from repository.contract_repository import ContractRepository
from repository.event_repository import EventRepository
from auth.auth_handler import AuthHandler
from models.role import Role
from models.collaborator import Collaborator
from models.contract import Contract
from models.event import Event
from models.client import Client


# Instanciate the DAOs
client_dao = ClientDao(session)
collaborator_dao = CollaboratorDao(session)
contract_dao = ContractDao(session)
event_dao = EventDao(session)


# Define the AppContainer (which purpose is to instanciate all the app components)
class AppContainer:
    def __init__(self):
        self.client_repo = ClientRepository(client_dao)
        self.collab_repo = CollaboratorRepository(collaborator_dao)
        self.contract_repo = ContractRepository(contract_dao)
        self.event_repo = EventRepository(event_dao)
        self.auth_handler = AuthHandler()

    def get_client_repo(self):
        return self.client_repo

    def get_collab_repo(self):
        return self.collab_repo

    def get_contract_repo(self):
        return self.contract_repo

    def get_event_repo(self):
        return self.event_repo

    def get_auth_handler(self):
        return self.auth_handler


# Instantiate the container
app_container = AppContainer()
