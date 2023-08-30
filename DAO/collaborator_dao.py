from models.collaborator import Collaborator
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input
from dao.sentry_context_manager import capture_exceptions
from sqlalchemy.exc import SQLAlchemyError


class CollaboratorDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, collaborator_id):
        with capture_exceptions():
            return self.db_session.get(Collaborator, collaborator_id)

    def get_all(self):
        with capture_exceptions():
            return self.db_session.query(Collaborator).all()

    def get_by_expression(self, filters):
        with capture_exceptions():
            filter_conditions = []
            for field, value in filters.items():
                column = getattr(Collaborator, field, None)
                if column is not None:
                    if sanitize_input(value) in ['false', 'False', 'none', 'None', '']:
                        filter_conditions.append(column.is_(None))
                    else:
                        filter_conditions.append(column == sanitize_input(value))
            # Combine the filter conditions using the 'and_' function
            combined_filter = and_(*filter_conditions)
            return self.db_session.query(Collaborator).filter(combined_filter)

    def get_by_username(self, username):
        with capture_exceptions():
            return self.db_session.query(Collaborator).filter(Collaborator.username == username).all()

    def create(self, collaborator):
        with capture_exceptions():
            try:
                self.db_session.add(collaborator)
                self.db_session.commit()
                return collaborator
            except SQLAlchemyError:
                return SQLAlchemyError

    def update(self, collaborator):
        with capture_exceptions():
            try:
                self.db_session.commit()
                return collaborator
            except SQLAlchemyError:
                return SQLAlchemyError

    def delete(self, collaborator):
        with capture_exceptions():
            self.db_session.delete(collaborator)
            self.db_session.commit()
