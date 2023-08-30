# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
# from models.client import Client
# from models.collaborator import Collaborator
# from models.contract import Contract
from models.event import Event
from repository.authorization_decorators import has_permission, is_events_support


class EventRepository:
    def __init__(self,
                 # client_dao,
                 event_dao,
                 # contract_dao,
                 # collaborator_dao
                 ):
        # self.client_dao = client_dao
        # self.contract_dao = contract_dao
        self.event_dao = event_dao
        # self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, event_id):
        return self.event_dao.fetch_by_id(event_id)

    @has_permission(permission="read_event")
    def get(self, token, filters):
        if filters != {}:
            return self.event_dao.get_by_expression(filters)
        return self.event_dao.get_all()

    @has_permission(permission="create_event")
    def create_event(self, token, event_data):
        event = Event(**event_data)
        self.event_dao.create(event)
        return [event]

    @has_permission(permission="update_event")
    @is_events_support
    def update_event(self, token, event_id, new_data):
        event = self.event_dao.fetch_by_id(event_id)
        if event:
            # Update user's data based on new_data
            event.title = new_data.get('title', event.title)
            event.start_date = new_data.get('start_date', event.start_date)
            event.end_date = new_data.get('end_date', event.end_date)
            event.location = new_data.get('location', event.location)
            event.attendees = new_data.get('attendees', event.attendees)
            event.comments = new_data.get('comments', event.comments)
            event.support_id = new_data.get('support_id', event.support_id)
            event.contract_id = new_data.get('contract_id', event.contract_id)
            self.event_dao.update(event)
            return [event]

    @has_permission(permission="delete_event")
    def delete_event(self, token, event_id):
        event = self.event_dao.fetch_by_id(event_id)
        if event:
            self.event_dao.delete(event)
            return [event]

    # def add_client(self)
    # def add_event(self)
