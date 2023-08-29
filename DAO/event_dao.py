from models.event import Event
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input


class EventDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, event_id):
        return self.db_session.get(Event, event_id)

    def get_all(self):
        return self.db_session.query(Event).all()

    def get_by_expression(self, filters):
        filter_conditions = []
        for field, value in filters.items():
            column = getattr(Event, field, None)
            if column is not None:
                filter_conditions.append(column == sanitize_input(value))
        # Combine the filter conditions using the 'and_' function
        combined_filter = and_(*filter_conditions)
        return self.db_session.query(Event).filter(combined_filter)

    def create(self, event):
        self.db_session.add(event)
        self.db_session.commit()

    def update(self, event):
        self.db_session.commit()

    def delete(self, event):
        self.db_session.delete(event)
        self.db_session.commit()
