from models.contract import Contract
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input
from dao.sentry_context_manager import capture_exceptions
from sqlalchemy.exc import SQLAlchemyError
import logging


class ContractDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, contract_id):
        with capture_exceptions():
            return self.db_session.get(Contract, contract_id)

    def get_all(self):
        with capture_exceptions():
            return self.db_session.query(Contract).all()

    def get_by_expression(self, filters):
        with capture_exceptions():
            filter_conditions = []
            for field, value in filters.items():
                column = getattr(Contract, field, None)
                if column is not None:
                    if sanitize_input(value) in ['false', 'False', 'none', 'None', '']:
                        filter_conditions.append(column.is_(None))
                    else:
                        filter_conditions.append(column == sanitize_input(value))
            print(filter_conditions)
            print(filters)
            # Combine the filter conditions using the 'and_' function
            combined_filter = and_(*filter_conditions)
            return self.db_session.query(Contract).filter(combined_filter)

    def create(self, contract):
        with capture_exceptions():
            try:
                self.db_session.add(contract)
                self.db_session.commit()
                return contract
            except SQLAlchemyError:
                return SQLAlchemyError

    def update(self, contract, signature):
        with capture_exceptions():
            try:
                self.db_session.commit()
                if signature:
                    logging.info(f"Contract signed: ID : {contract.id},"
                                 f"Legal ID : {contract.legal_id},"
                                 f"Client : {str(contract.client)}"
                                 f"Event : {str(contract.event)}")
                    logging.error("CONTRACT SIGNED")
                return contract
            except SQLAlchemyError:
                return SQLAlchemyError

    def delete(self, contract):
        with capture_exceptions():
            self.db_session.delete(contract)
            self.db_session.commit()
