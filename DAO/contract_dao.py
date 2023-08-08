from models import Contract


class ContractDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, collaborator_id):
        return self.db_session.query(Contract).get(collaborator_id)

    def save(self, user):
        self.db_session.add(user)
        self.db_session.commit()

    def update(self, user):
        self.db_session.commit()

    def delete(self, user):
        self.db_session.delete(user)
        self.db_session.commit()
