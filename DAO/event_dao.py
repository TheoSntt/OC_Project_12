from models.event import Event


class EventDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, event_id):
        return self.db_session.get(Event, event_id)

    def get_all(self):
        return self.db_session.query(Event).all()

    def get_by_expression(self, expression):
        return self.db_session.query(Event).filter(expression).all()

    def create(self, event):
        self.db_session.add(event)
        self.db_session.commit()

    def update(self, event):
        self.db_session.commit()

    def delete(self, event):
        self.db_session.delete(event)
        self.db_session.commit()
