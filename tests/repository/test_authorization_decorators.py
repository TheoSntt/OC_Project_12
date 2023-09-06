from repository.authorization_decorators import (has_permission, is_clients_contact,
                                                 is_contracts_clients_contact, is_events_support)
import jwt


class DumbClient():
    def __init__(self, id, contact_id):
        self.id = id
        self.contact_id = contact_id


class DumbContract():
    def __init__(self, id, client):
        self.id = id
        self.client = client


class DumbEvent():
    def __init__(self, id, support_id):
        self.id = id
        self.support_id = support_id


class DumbClass():
    @has_permission("needed_permission")
    def decorated_method(self, token):
        return "Authorized !"

    @is_clients_contact
    def decorated_client_method(self, token, client_id):
        return "Authorized !"

    def get_by_id(self, id):
        return DumbClient(id, 2)


class DumbClassContract():
    @is_contracts_clients_contact
    def decorated_contract_method(self, token, contract_id):
        return "Authorized !"

    def get_by_id(self, id):
        return DumbContract(id, DumbClient(1, 2))


class DumbClassEvent():
    @is_events_support
    def decorated_event_method(self, token, event_id):
        return "Authorized !"

    def get_by_id(self, id):
        return DumbEvent(id, 2)


class TestAuthorizationDecorators:
    def test_has_permission_valid_token_and_permission(self, mocker):
        moked_payload = {
            "user_permissions": ["needed_permission", "some_other_permission"]
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClass()
        result = dummy.decorated_method("some_valid_token")
        assert result == "Authorized !"

    def test_has_permission_valid_token_no_permission(self, mocker):
        moked_payload = {
            "user_permissions": ["some_other_permission"]
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClass()
        result = dummy.decorated_method("some_valid_token")
        assert result is None

    def test_has_permission_invalid_token(self, mocker):
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=jwt.DecodeError)
        dummy = DumbClass()
        result = dummy.decorated_method("some_valid_token")
        assert result == jwt.DecodeError

    def test_is_clients_contact_user_is_admin(self, mocker):
        moked_payload = {
            "user_role": "Admin"
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClass()
        result = dummy.decorated_client_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_clients_contact_user_is_sales_and_contact(self, mocker):
        moked_payload = {
            "user_role": "Sales",
            'user_id': 2
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClass()
        result = dummy.decorated_client_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_clients_contact_user_is_sales_but_not_contact(self, mocker):
        moked_payload = {
            "user_role": "Sales",
            'user_id': 1
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClass()
        result = dummy.decorated_client_method("some_valid_token", 1)
        assert result is None

    def test_is_contracts_clients_contact_user_is_admin(self, mocker):
        moked_payload = {
            "user_role": "Admin"
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassContract()
        result = dummy.decorated_contract_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_contracts_clients_contact_user_is_sales_and_contact(self, mocker):
        moked_payload = {
            "user_role": "Sales",
            'user_id': 2
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassContract()
        result = dummy.decorated_contract_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_contracts_clients_contact_user_is_sales_but_not_contact(self, mocker):
        moked_payload = {
            "user_role": "Sales",
            'user_id': 1
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassContract()
        result = dummy.decorated_contract_method("some_valid_token", 1)
        assert result is None

    def test_is_events_support_user_is_admin(self, mocker):
        moked_payload = {
            "user_role": "Admin"
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassEvent()
        result = dummy.decorated_event_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_events_support_user_is_support_and_event_support(self, mocker):
        moked_payload = {
            "user_role": "Support",
            'user_id': 2
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassEvent()
        result = dummy.decorated_event_method("some_valid_token", 1)
        assert result == "Authorized !"

    def test_is_is_events_support_user_is_support_but_not_event_support(self, mocker):
        moked_payload = {
            "user_role": "Support",
            'user_id': 1
        }
        mocker.patch("auth.auth_handler.AuthHandler.verify_token", return_value=moked_payload)
        dummy = DumbClassEvent()
        result = dummy.decorated_event_method("some_valid_token", 1)
        assert result is None
