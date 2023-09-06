from repository.authorization_decorators import has_permission, is_clients_contact
import jwt


class DumbClass():
    @has_permission("needed_permission")
    def decorated_method(self, token):
        return "Authorized !"

    @is_clients_contact
    def decorated_client_method(self, token):
        return "Authorized !"


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
