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


def mock_decorator_bis(function):
    @wraps(function)
    def wrapper(instance, *args, **kwargs):
        result = function(instance, *args, **kwargs)
        return result
    return wrapper


patch('repository.authorization_decorators.has_permission', mock_decorator).start()
patch('repository.authorization_decorators.is_clients_contact', mock_decorator_bis).start()


from repository.client_repository import ClientRepository


class TestClientRepository:

    def test_get_by_id(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a client"
        sut = ClientRepository(DAO_mock)
        assert sut.get_by_id(1) == "a client"

    def test_get_without_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_all.return_value = "all clients"
        sut = ClientRepository(DAO_mock)
        assert sut.get("token", {}) == "all clients"

    def test_get_with_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_by_expression.return_value = "some clients"
        sut = ClientRepository(DAO_mock)
        assert sut.get("token", {"field": "value"}) == "some clients"

    def test_create(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.create.return_value = "created client"
        sut = ClientRepository(DAO_mock)
        client_data = {
            "name": "Bob",
            "surname": "Morane",
            "email": "bob.morane@laventurier.fr",
            "telephone": "0168753434",
            "enterprise_name": "Indochine",
            "contact_id": "1"
        }
        result = sut.create_client("token", client_data)
        assert result == "created client"

    def test_update(self, mocker):
        class DumbClient():
            def __init__(self, id, name, surname, email, telephone, enterprise_name, contact_id):
                self.id = id
                self.name = name
                self.surname = surname
                self.email = email
                self.telephone = telephone
                self.enterprise_name = enterprise_name
                self.contact_id = contact_id
        dummyclient = DumbClient(1, "Jean", "Client", "j.c@mail.fr", "010101010101", "Entreprise", 1)
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = dummyclient
        DAO_mock.update.return_value = "updated_client"
        sut = ClientRepository(DAO_mock)
        new_data = {
            "name": "Bob",
            "surname": "Morane"
        }
        result = sut.update_client("token", 1, new_data)
        assert result == "updated_client"

    def test_delete(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a client"
        sut = ClientRepository(DAO_mock)
        result = sut.delete_client("token", 1)
        assert result == "a client"

