# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
# from models.client import Client
# from models.collaborator import Collaborator
# from models.contract import Contract
from models.event import Event


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

    # def get_client_events(self, event_id):
    #     return self.event_dao.get_events_for_user(event_id)

    def create_event(self, event_data):
        event = Event(**event_data)
        self.event_dao.create(event)
        return event

    def update_eventt(self, event_id, new_data):
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

    def delete_event(self, event_id):
        event = self.event_dao.fetch_by_id(event_id)
        if event:
            self.event_dao.delete(event)

    # def add_client(self)
    # def add_event(self)
