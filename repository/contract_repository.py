# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
# from models.client import Client
# from models.collaborator import Collaborator
from models.contract import Contract
# from models.event import Event
from datetime import date
from repository.authorization_decorators import has_permission, is_contracts_clients_contact


class ContractRepository:
    def __init__(self,
                 # client_dao,
                 contract_dao,
                 # event_dao,
                 # collaborator_dao
                 ):
        # self.client_dao = client_dao
        self.contract_dao = contract_dao
        # self.event_dao = event_dao
        # self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, contract_id):
        return self.contract_dao.fetch_by_id(contract_id)

    @has_permission(permission="read_contract")
    def get(self, token, filters):
        if filters != {}:
            return self.contract_dao.get_by_expression(filters)
        return self.contract_dao.get_all()

    @has_permission(permission="create_contract")
    def create_contract(self, token, contract_data):
        contract = Contract(**contract_data,
                            create_date=date.today())
        contract = self.contract_dao.create(contract)
        return contract

    @has_permission(permission="update_contract")
    @is_contracts_clients_contact
    def update_contract(self, token, contract_id, new_data):
        contract = self.contract_dao.fetch_by_id(contract_id)
        if contract:
            # Update user's data based on new_data
            contract.legal_id = new_data.get('legal_id', contract.legal_id)
            contract.price = new_data.get('price', contract.price)
            contract.remaining_to_pay = new_data.get('remaining_to_pay', contract.remaining_to_pay)
            # contract.create_date = new_data.get('create_date', contract.create_date)
            contract.status = new_data.get('status', contract.status)
            contract.client_id = new_data.get('client_id', contract.client_id)
            contract = self.contract_dao.update(contract)
            return contract

    @has_permission(permission="delete_contract")
    def delete_contract(self, token, contract_id):
        contract = self.contract_dao.fetch_by_id(contract_id)
        if contract:
            self.contract_dao.delete(contract)
            return contract

    # def add_client(self)
    # def add_event(self)
