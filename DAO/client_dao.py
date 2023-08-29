from models.client import Client
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input


class ClientDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, client_id):
        return self.db_session.get(Client, client_id)

    def get_all(self):
        return self.db_session.query(Client).all()

    def get_by_expression(self, filters):
        filter_conditions = []
        for field, value in filters.items():
            column = getattr(Client, field, None)
            if column is not None:
                filter_conditions.append(column == sanitize_input(value))
        # Combine the filter conditions using the 'and_' function
        combined_filter = and_(*filter_conditions)
        return self.db_session.query(Client).filter(combined_filter)

    def create(self, client):
        self.db_session.add(client)
        self.db_session.commit()

    def update(self, client):
        self.db_session.commit()

    def delete(self, client):
        self.db_session.delete(client)
        self.db_session.commit()
