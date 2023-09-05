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
patch('repository.authorization_decorators.is_contracts_clients_contact', mock_decorator_bis).start()


from repository.contract_repository import ContractRepository


class TestContractRepository:

    def test_get_by_id(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a contract"
        sut = ContractRepository(DAO_mock)
        assert sut.get_by_id(1) == "a contract"

    def test_get_without_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_all.return_value = "all contracts"
        sut = ContractRepository(DAO_mock)
        assert sut.get("token", {}) == "all contracts"

    def test_get_with_filters(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.get_by_expression.return_value = "some contracts"
        sut = ContractRepository(DAO_mock)
        assert sut.get("token", {"field": "value"}) == "some contracts"

    def test_create(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.create.return_value = "created contract"
        sut = ContractRepository(DAO_mock)
        contract_data = {
            "legal_id": "123A",
            "price": 1500,
            "remaining_to_pay": 1400,
            "status": "En cours",
            "client_id": "1"
        }
        result = sut.create_contract("token", contract_data)
        assert result == "created contract"

    def test_update(self, mocker):
        class DumbContract():
            def __init__(self, id, legal_id, price, remaining_to_pay, status, client_id):
                self.id = id
                self.legal_id = legal_id
                self.price = price
                self.remaining_to_pay = remaining_to_pay
                self.status = status
                self.client_id = client_id
        dummycontract = DumbContract(1, "123A", 1500, 1500, "En cours", 1)
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = dummycontract
        DAO_mock.update.return_value = "updated contract"
        sut = ContractRepository(DAO_mock)
        new_data = {
            "legal_id": "123B",
            "price": 2500,
        }
        result = sut.update_contract("token", 1, new_data)
        assert result == "updated contract"

    def test_delete(self, mocker):
        DAO_mock = mocker.Mock()
        DAO_mock.fetch_by_id.return_value = "a contract"
        sut = ContractRepository(DAO_mock)
        result = sut.delete_contract("token", 1)
        assert result == "a contract"

