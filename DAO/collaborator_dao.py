from models.collaborator import Collaborator


class CollaboratorDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, collaborator_id):
        return self.db_session.get(Collaborator, collaborator_id)

    def get_by_expression(self, expression):
        return self.db_session.query(Collaborator).filter(expression).all()

    def create(self, collaborator):
        self.db_session.add(collaborator)
        self.db_session.commit()

    def update(self, collaborator):
        self.db_session.commit()

    def delete(self, collaborator):
        self.db_session.delete(collaborator)
        self.db_session.commit()
