# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
# from models.client import Client
from models.collaborator import Collaborator
# from models.contract import Contract
# from models.event import Event


class CollaboratorRepository:
    def __init__(self, client_dao, contract_dao, event_dao, collaborator_dao):
        # self.client_dao = client_dao
        # self.contract_dao = contract_dao
        # self.event_dao = event_dao
        self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, collaborator_id):
        return self.collaborator_dao.fetch_by_id(collaborator_id)

    # def get_collaborator_events(self, collaborator_id):
    #     return self.event_dao.get_events_for_user(collaborator_id)

    def create_collaborator(self, collaborator_data):
        collaborator = Collaborator(**collaborator_data)
        self.collaborator_dao.save(collaborator)

    def update_collaborator(self, collaborator_id, new_data):
        collaborator = self.collaborator_dao.fetch_by_id(collaborator_id)
        if collaborator:
            # Update user's data based on new_data
            collaborator.name = new_data.get('name', collaborator.name)
            collaborator.surname = new_data.get('surname', collaborator.surname)
            collaborator.email = new_data.get('email', collaborator.email)
            collaborator.telephone = new_data.get('telephone', collaborator.telephone)
            collaborator.role = new_data.get('role', collaborator.role)
            self.collaborator_dao.update(collaborator)

    def delete_collaborator(self, collaborator_id):
        collaborator = self.collaborator_dao.fetch_by_id(collaborator_id)
        if collaborator:
            self.collaborator_dao.delete(collaborator)

    # def add_client(self)
    # def add_event(self)
