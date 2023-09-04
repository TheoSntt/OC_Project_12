from auth.jwt.jwt_handler import JWTHandler
import pytest
import jwt
# import auth.jwt.jwt_handler as jwt_handler
# from auth.jwt import jwt_handler


def test_should_load_key(mocker):
    sut = JWTHandler()
    mocker.patch("os.environ.get", return_value="Top_Secret_Key")
    expected_value = "Top_Secret_Key"
    sut._load_secret_key()
    assert sut.secret_key == expected_value


def test_should_raise_if_missing_key(mocker):
    sut = JWTHandler()
    mocker.patch("os.environ.get", return_value=None)
    with pytest.raises(ValueError, match="JWT_SECRET_KEY environment variable is not set"):
        sut._load_secret_key()


def test_should_clear_key(mocker):
    sut = JWTHandler()
    mocker.patch("os.environ.get", return_value="Top_Secret_Key")
    sut._load_secret_key()
    sut._clear_secret_key()
    assert sut.secret_key is None


def test_should_generate_token(mocker):
    sut = JWTHandler()
    mocker.patch("jwt.encode", return_value="Some_coded_token")
    token = sut.generate_token({"payload": "data"})
    expected_value = "Some_coded_token"
    assert sut.secret_key is None
    assert token == expected_value


def test_should_return_payload(mocker):
    sut = JWTHandler()
    mocker.patch("jwt.decode", return_value="Some_decoded_payload")
    payload = sut.verify_jwt_token("a token")
    expected_value = "Some_decoded_payload"
    assert sut.secret_key is None
    assert payload == expected_value


def test_should_return_Expired_Error(mocker):
    sut = JWTHandler()
    mocker.patch("jwt.decode", side_effect=jwt.ExpiredSignatureError)
    payload = sut.verify_jwt_token("a token")
    expected_value = jwt.ExpiredSignatureError
    assert sut.secret_key is None
    assert payload == expected_value


def test_should_return_Decode_Error(mocker):
    sut = JWTHandler()
    mocker.patch("jwt.decode", side_effect=jwt.DecodeError)
    payload = sut.verify_jwt_token("a token")
    expected_value = jwt.DecodeError
    assert sut.secret_key is None
    assert payload == expected_value
