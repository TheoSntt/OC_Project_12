# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
from models.client import Client
# from models.collaborator import Collaborator
# from models.contract import Contract
# from models.event import Event
from datetime import date
from repository.has_permission_decorator import has_permission


class ClientRepository:
    def __init__(self,
                 client_dao,
                 # contract_dao,
                 # event_dao,
                 # collaborator_dao
                 ):
        self.client_dao = client_dao
        # self.contract_dao = contract_dao
        # self.event_dao = event_dao
        # self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, client_id):
        return self.client_dao.fetch_by_id(client_id)

    @has_permission(permission="read_client")
    def get(self, token, filters):
        if filters != {}:
            return self.client_dao.get_by_expression(filters)
        return self.client_dao.get_all()
    # def get_client_events(self, client_id):
    #     return self.event_dao.get_events_for_user(client_id)

    @has_permission(permission="create_client")
    def create_client(self, token, client_data):
        client = Client(**client_data,
                        create_date=date.today(),
                        last_update_date=date.today())
        # client.create_date = date.today()
        # client.last_update_date = date.today()
        self.client_dao.create(client)
        return [client]

    @has_permission(permission="update_client")
    def update_client(self, token, client_id, new_data):
        client = self.client_dao.fetch_by_id(client_id)
        if client:
            # Update user's data based on new_data
            client.name = new_data.get('name', client.name)
            client.surname = new_data.get('surname', client.surname)
            client.email = new_data.get('email', client.email)
            client.telephone = new_data.get('telephone', client.telephone)
            client.enterprise_name = new_data.get('enterprise_name', client.enterprise_name)
            # client.create_date = new_data.get('create_date', client.create_date)
            client.last_update_date = date.today()
            client.contact_id = new_data.get('contact_id', client.contact_id)
            self.client_dao.update(client)
            return [client]

    @has_permission(permission="delete_client")
    def delete_client(self, token, client_id):
        client = self.client_dao.fetch_by_id(client_id)
        if client:
            self.client_dao.delete(client)
            return [client]

    # def add_client(self)
    # def add_event(self)
