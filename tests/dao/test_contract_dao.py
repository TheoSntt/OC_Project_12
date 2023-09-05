from dao.contract_dao import ContractDao
from models.contract import Contract
from sqlalchemy.exc import SQLAlchemyError
from unittest.mock import call


class TestContractDao:

    def test_fetch_by_id(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.get.return_value = "an contract"
        sut = ContractDao(db_session_mock)
        assert sut.fetch_by_id(1) == "an contract"

    def test_get_all(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Contract).all.return_value = "all contracts"
        sut = ContractDao(db_session_mock)
        assert sut.get_all() == "all contracts"

    def test_get_by_expression(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.query(Contract).filter.return_value = "some contracts"
        sut = ContractDao(db_session_mock)
        result = sut.get_by_expression({'client_id': '3', 'status': 'false'})
        assert result == "some contracts"

    def test_create(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ContractDao(db_session_mock)
        result = sut.create("a new contract")
        assert result == "a new contract"
        calls = [call.add('a new contract'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_create_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = ContractDao(db_session_mock)
        result = sut.create("a new contract")
        assert result == SQLAlchemyError
        calls = [call.add('a new contract'), call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_update_not_signed(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ContractDao(db_session_mock)
        result = sut.update("an contract", False)
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)
        assert result == "an contract"

    def test_update_signed(self, mocker):
        class DumbContract():
            def __init__(self, id, legal_id, client, event):
                self.id = id
                self.legal_id = legal_id
                self.client = client
                self.event = event
        db_session_mock = mocker.Mock()
        sut = ContractDao(db_session_mock)
        dummycontract = DumbContract(1, 12, "client", "event")
        result = sut.update(dummycontract, True)
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)
        assert result == dummycontract

    def test_update_Integrity_error(self, mocker):
        db_session_mock = mocker.Mock()
        db_session_mock.commit.side_effect = SQLAlchemyError
        sut = ContractDao(db_session_mock)
        result = sut.update("a contract", False)
        assert result == SQLAlchemyError
        calls = [call.commit()]
        db_session_mock.assert_has_calls(calls)

    def test_delete(self, mocker):
        db_session_mock = mocker.Mock()
        sut = ContractDao(db_session_mock)
        sut.delete("an contract")
        calls = [call.delete('an contract'), call.commit()]
        db_session_mock.assert_has_calls(calls)
