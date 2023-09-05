from dao.event_dao import EventDao
from models.event import Event
from sqlalchemy.exc import SQLAlchemyError
from unittest.mock import call


class TestEventDAO:

    def test_fetch_by_id(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.get.return_value = "an event"
        sut = EventDao(db_session_mock)
        assert sut.fetch_by_id(1) == "an event"

    def test_get_all(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Event).all.return_value = "all events"
        sut = EventDao(db_session_mock)
        assert sut.get_all() == "all events"

    def test_get_by_expression(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Event).filter.return_value = "some events"
        sut = EventDao(db_session_mock)
        result = sut.get_by_expression({'support_id': '3', 'location': 'false'})
        assert result == "some events"

    def test_create(self, mocker):
        db_session_mock = mocker.Mock()
        sut = EventDao(db_session_mock)
        result = sut.create("a new event")
        assert result == "a new event"
        calls = [call.add('a new event'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_create_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = EventDao(db_session_mock)
        result = sut.create("a new event")
        assert result == SQLAlchemyError
        calls = [call.add('a new event'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_update(self, mocker):
        db_session_mock = mocker.Mock()
        sut = EventDao(db_session_mock)
        result = sut.update("an event")
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)
        assert result == "an event"

    def test_update_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = EventDao(db_session_mock)
        result = sut.update("an event")
        assert result == SQLAlchemyError
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_delete(self, mocker):
        db_session_mock = mocker.Mock()
        sut = EventDao(db_session_mock)
        sut.delete("an event")
        calls = [call.delete('an event'), call.commit()]
        db_session_mock.assert_has_calls(calls)
