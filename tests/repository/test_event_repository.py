from functools import wraps
from unittest.mock import patch
from models.event import Event
from models.contract import Contract
from models.client import Client
from models.collaborator import Collaborator
from models.role import Role
from datetime import date


def mock_decorator(*args, **kwargs):
    """Decorate by doing nothing."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def mock_decorator_bis(function):
    @wraps(function)
    def wrapper(instance, *args, **kwargs):
        result = function(instance, *args, **kwargs)
        return result
    return wrapper


patch('repository.authorization_decorators.has_permission', mock_decorator).start()
patch('repository.authorization_decorators.is_events_support', mock_decorator_bis).start()


from repository.event_repository import EventRepository


class TestEventRepository:

    def test_get_by_id(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a event"
        sut = EventRepository(DAO_mock)
        assert sut.get_by_id(1) == "a event"

    def test_get_without_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_all.return_value = "all events"
        sut = EventRepository(DAO_mock)
        assert sut.get("token", {}) == "all events"

    def test_get_with_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_by_expression.return_value = "some events"
        sut = EventRepository(DAO_mock)
        assert sut.get("token", {"field": "value"}) == "some events"

    def test_create(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.create.return_value = "created event"
        sut = EventRepository(DAO_mock)
        event_data = {
            "title": "event",
            "start_date": date(2023, 9, 30),
            "end_date": date(2023, 9, 30),
            "location": "ici",
            "attendees": 240,
            "comments": "",
            "support_id": "1",
            "contract_id": "1"

        }
        result = sut.create_event("token", event_data)
        assert result == "created event"

    def test_update(self, mocker):
        class DumbEvent():
            def __init__(self, id, title, start_date, end_date, location,
                         attendees, comments, support_id, contract_id):
                self.id = id
                self.title = title
                self.start_date = start_date
                self.end_date = end_date
                self.location = location
                self.attendees = attendees
                self.comments = comments
                self.support_id = support_id
                self.contract_id = contract_id
        dummyevent = DumbEvent(1, "event", date(2023, 9, 30), date(2023, 9, 30), "ici", 20, "", 1, 1)
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = dummyevent
        DAO_mock.update.return_value = "updated_event"
        sut = EventRepository(DAO_mock)
        new_data = {
            "location": "là bas",
            "attendees": 260,
        }
        result = sut.update_event("token", 1, new_data)
        assert result == "updated_event"

    def test_delete(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a event"
        sut = EventRepository(DAO_mock)
        result = sut.delete_event("token", 1)
        assert result == "a event"
