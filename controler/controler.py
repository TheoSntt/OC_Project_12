# from repository.client_repository import ClientRepository
# from repository.collaborator_repository import CollaboratorRepository
# from repository.contract_repository import ContractRepository
# from repository.event_repository import EventRepository


class Controler:
    def __init__(self, clientrepo, collabrepo, contractrepo, eventrepo):
        self.clientrepo = clientrepo
        self.collabrepo = collabrepo
        self.contractrepo = contractrepo
        self.eventrepo = eventrepo

    def get_all_collabs(self):
        self.collabrepo.get_all()
    
    def get_all_clients(self):
        self.clientrepo.get_all()
    
    def get_all_contracts(self):
        self.contractrepo.get_all()
    
    def get_all_events(self):
        self.eventrepo.get_all()
