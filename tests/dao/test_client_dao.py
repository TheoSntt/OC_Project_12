from dao.client_dao import ClientDao
from models.client import Client
from sqlalchemy.exc import SQLAlchemyError
from unittest.mock import call


class TestClientDAO:

    def test_fetch_by_id(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.get.return_value = "a client"
        sut = ClientDao(db_session_mock)
        assert sut.fetch_by_id(1) == "a client"

    def test_get_all(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Client).all.return_value = "all clients"
        sut = ClientDao(db_session_mock)
        assert sut.get_all() == "all clients"

    def test_get_by_expression(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Client).filter.return_value = "some clients"
        sut = ClientDao(db_session_mock)
        result = sut.get_by_expression({'contact_id': '1', 'name': ''})
        assert result == "some clients"

    def test_create(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ClientDao(db_session_mock)
        result = sut.create("a new client")
        assert result == "a new client"
        calls = [call.add('a new client'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_create_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = ClientDao(db_session_mock)
        result = sut.create("a new client")
        assert result == SQLAlchemyError
        calls = [call.add('a new client'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_update(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ClientDao(db_session_mock)
        result = sut.update("a client")
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)
        assert result == "a client"

    def test_update_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = ClientDao(db_session_mock)
        result = sut.update("an client")
        assert result == SQLAlchemyError
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_delete(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ClientDao(db_session_mock)
        sut.delete("a client")
        calls = [call.delete('a client'), call.commit()]
        db_session_mock.assert_has_calls(calls)
