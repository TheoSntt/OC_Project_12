from models import Client


class ClientDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, client_id):
        return self.db_session.get(Client, client_id)

    def get_by_expression(self, expression):
        return self.db_session.query(Client).filter(expression).all()

    def create(self, client):
        self.db_session.add(client)
        self.db_session.commit()

    def update(self, client):
        self.db_session.commit()

    def delete(self, client):
        self.db_session.delete(client)
        self.db_session.commit()
