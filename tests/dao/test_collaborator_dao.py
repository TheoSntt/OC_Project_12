from dao.collaborator_dao import CollaboratorDao
from models.collaborator import Collaborator
from sqlalchemy.exc import SQLAlchemyError
from unittest.mock import call


class TestCollaboratorDAO:

    def test_fetch_by_id(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.get.return_value = "a collaborator"
        sut = CollaboratorDao(db_session_mock)
        assert sut.fetch_by_id(1) == "a collaborator"

    def test_get_by_usernmame(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Collaborator).filter.return_value.all.return_value = "Bob the collaborator"
        sut = CollaboratorDao(db_session_mock)
        result = sut.get_by_username("Bob")
        assert result == "Bob the collaborator"

    def test_get_all(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Collaborator).all.return_value = "all collaborators"
        sut = CollaboratorDao(db_session_mock)
        assert sut.get_all() == "all collaborators"

    def test_get_by_expression(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Collaborator).filter.return_value = "some collaborators"
        sut = CollaboratorDao(db_session_mock)
        result = sut.get_by_expression({'role_id': '1', 'name': ''})
        assert result == "some collaborators"

    def test_create(self, mocker):
        class DumbCollab():
            def __init__(self, id, name, role):
                self.id = id
                self.name = name
                self.role = role
        dummycollab = DumbCollab(1, "Jean", "Admin")
        db_session_mock = mocker.Mock()
        sut = CollaboratorDao(db_session_mock)
        result = sut.create(dummycollab)
        assert result == dummycollab
        calls = [call.add(dummycollab), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_create_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = CollaboratorDao(db_session_mock)
        result = sut.create("a new collaborator")
        assert result == SQLAlchemyError
        calls = [call.add('a new collaborator'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_update(self, mocker):
        class DumbCollab():
            def __init__(self, id, name, role):
                self.id = id
                self.name = name
                self.role = role
        dummycollab = DumbCollab(1, "Jean", "Admin")
        db_session_mock = mocker.Mock()
        sut = CollaboratorDao(db_session_mock)
        result = sut.update(dummycollab)
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)
        assert result == dummycollab

    def test_update_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = CollaboratorDao(db_session_mock)
        result = sut.update("a collaborator")
        assert result == SQLAlchemyError
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_delete(self, mocker):
        db_session_mock = mocker.Mock()
        sut = CollaboratorDao(db_session_mock)
        sut.delete("a collaborator")
        calls = [call.delete('a collaborator'), call.commit()]
        db_session_mock.assert_has_calls(calls)
