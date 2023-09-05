from functools import wraps
from unittest.mock import patch
from models.collaborator import Collaborator
from models.contract import Contract
from models.client import Client
from models.event import Event
from models.role import Role


def mock_decorator(*args, **kwargs):
    """Decorate by doing nothing."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    return decorator


patch('repository.authorization_decorators.has_permission', mock_decorator).start()


from repository.collaborator_repository import CollaboratorRepository


class TestCollaboratorRepository:

    def test_get_by_id(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a collaborator"
        sut = CollaboratorRepository(DAO_mock)
        assert sut.get_by_id(1) == "a collaborator"

    def test_get_without_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_all.return_value = "all collaborators"
        sut = CollaboratorRepository(DAO_mock)
        assert sut.get("token", {}) == "all collaborators"

    def test_get_with_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_by_expression.return_value = "some collaborators"
        sut = CollaboratorRepository(DAO_mock)
        assert sut.get("token", {"field": "value"}) == "some collaborators"

    def test_create(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.create.return_value = "created collaborator"
        sut = CollaboratorRepository(DAO_mock)
        collaborator_data = {
            "name": "Bob",
            "surname": "Morane",
            "email": "bob.morane@laventurier.fr",
            "telephone": "0168753434",
            "username": "bobmorane",
            "password": "80sF3v3r",
            "role_id": "1"
        }
        result = sut.create_collaborator("token", collaborator_data)
        assert result == "created collaborator"

    def test_update(self, mocker):
        class DumbCollaborator():
            def __init__(self, id, name, surname, email, telephone, username, password, role_id):
                self.id = id
                self.name = name
                self.surname = surname
                self.email = email
                self.telephone = telephone
                self.username = username
                self.password = password
                self.role_id = role_id
        dummycollaborator = DumbCollaborator(1, "Jean", "Collaborator", "j.c@mail.fr", "010101010101", "jean", "pw", 1)
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = dummycollaborator
        DAO_mock.update.return_value = "updated_collaborator"
        sut = CollaboratorRepository(DAO_mock)
        new_data = {
            "name": "Bob",
            "surname": "Morane"
        }
        result = sut.update_collaborator("token", 1, new_data)
        assert result == "updated_collaborator"

    def test_delete(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a collaborator"
        sut = CollaboratorRepository(DAO_mock)
        result = sut.delete_collaborator("token", 1)
        assert result == "a collaborator"

