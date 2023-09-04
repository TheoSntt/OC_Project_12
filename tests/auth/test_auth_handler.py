from auth.auth_handler import AuthHandler
# from auth.crypt_context import cryptcontext
# from auth.jwt.jwt_handler import JWTHandler


def test_should_hash(mocker):
    sut = AuthHandler()
    hash_password_mock = mocker.patch.object(sut.cryptcontext, 'hash')
    hash_password_mock.return_value = "SOMEHASHEDPASSWORD"
    expected_value = "SOMEHASHEDPASSWORD"
    assert sut.hash_password("pw") == expected_value


def test_should_confirm(mocker):
    sut = AuthHandler()
    verify_password_mock = mocker.patch.object(sut.cryptcontext, 'verify')
    verify_password_mock.return_value = True
    assert sut.verify_password("thats_some_bad_password_harry", "SOMEHASHEDPASSWORD") is True


def test_should_not_confirm(mocker):
    sut = AuthHandler()
    verify_password_mock = mocker.patch.object(sut.cryptcontext, 'verify')
    verify_password_mock.return_value = False
    assert sut.verify_password("thats_some_other_password", "SOMEHASHEDPASSWORD") is False


def test_verify_login_attempt_should_succeed(mocker):
    # Create a mock collaborator object
    class UserObject:
        def __init__(self, username, password, role, id):
            self.username = username
            self.password = password
            self.role = role
            self.id = id
    # Create a mock object for collab_repo
    collab_repo_mock = mocker.Mock()
    user = UserObject("bobdu34", "password123", "Admin", "2")
    collab_repo_mock.get_by_username.return_value = [user]
    sut = AuthHandler()
    # Create a mock for the self.verify_password method
    verify_password_mock = mocker.patch.object(sut, 'verify_password')
    # Set the return value of the verify_something mock
    verify_password_mock.return_value = True
    # Call the verify_login_attempt method with the mock collab_repo
    result = sut.verify_login_attempt(collab_repo_mock, "bobdu34", "password123")
    assert 'token' in result


def test_verify_login_attempt_should_fail_wrong_username(mocker):
    # Create a mock object for collab_repo
    collab_repo_mock = mocker.Mock()
    collab_repo_mock.get_by_username.return_value = []
    sut = AuthHandler()
    # Create a mock for the self.verify_password method
    verify_password_mock = mocker.patch.object(sut, 'verify_password')
    # Set the return value of the verify_something mock
    verify_password_mock.return_value = True
    # Call the verify_login_attempt method with the mock collab_repo
    result = sut.verify_login_attempt(collab_repo_mock, "bobdu36", "password123")
    assert result is False


def test_verify_login_attempt_should_fail_wrong_pw(mocker):
    # Create a mock collaborator object
    class UserObject:
        def __init__(self, username, password, role, id):
            self.username = username
            self.password = password
            self.role = role
            self.id = id
    # Create a mock object for collab_repo
    collab_repo_mock = mocker.Mock()
    user = UserObject("bobdu34", "password123", "Admin", "2")
    collab_repo_mock.get_by_username.return_value = [user]
    sut = AuthHandler()
    # Create a mock for the self.verify_password method
    verify_password_mock = mocker.patch.object(sut, 'verify_password')
    # Set the return value of the verify_something mock
    verify_password_mock.return_value = False
    # Call the verify_login_attempt method with the mock collab_repo
    result = sut.verify_login_attempt(collab_repo_mock, "bobdu34", "password123")
    assert result is False


def test_verify_token(mocker):
    sut = AuthHandler()
    verify_token_mock = mocker.patch.object(sut.jwt_handler, 'verify_jwt_token')
    verify_token_mock.return_value = {"payload": "data"}
    expected_value = {"payload": "data"}
    payload = sut.verify_token("some_token")
    assert payload == expected_value
