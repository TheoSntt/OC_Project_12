from models.client import Client
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input
from dao.sentry_context_manager import capture_exceptions
from sqlalchemy.exc import SQLAlchemyError


class ClientDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, client_id):
        with capture_exceptions():
            return self.db_session.get(Client, client_id)

    def get_all(self):
        with capture_exceptions():
            return self.db_session.query(Client).all()

    def get_by_expression(self, filters):
        with capture_exceptions():
            filter_conditions = []
            for field, value in filters.items():
                column = getattr(Client, field, None)
                if column is not None:
                    if sanitize_input(value) in ['false', 'False', 'none', 'None', '']:
                        filter_conditions.append(column.is_(None))
                    else:
                        filter_conditions.append(column == sanitize_input(value))
            # Combine the filter conditions using the 'and_' function
            combined_filter = and_(*filter_conditions)
            return self.db_session.query(Client).filter(combined_filter).all()

    def create(self, client):
        with capture_exceptions():
            try:
                self.db_session.add(client)
                self.db_session.commit()
                return client
            except SQLAlchemyError:
                return SQLAlchemyError

    def update(self, client):
        with capture_exceptions():
            try:
                self.db_session.commit()
                return client
            except SQLAlchemyError:
                return SQLAlchemyError

    def delete(self, client):
        with capture_exceptions():
            self.db_session.delete(client)
            self.db_session.commit()
