from models.contract import Contract
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input
from dao.sentry_context_manager import capture_exceptions
from sqlalchemy.exc import SQLAlchemyError
import logging
import sentry_sdk
import os
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


# sentry_sdk.init(
#     dsn=os.environ.get("SENTRY_DSN"),
#     integrations=[SqlalchemyIntegration(),
#                   LoggingIntegration(level=logging.INFO)]
#             )


class ContractDao:
    def __init__(self, db_session):
        self.db_session = db_session
        sentry_sdk.init(
            dsn=os.environ.get("SENTRY_DSN"),
            integrations=[SqlalchemyIntegration(), LoggingIntegration(level=logging.INFO)]
            )

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
                    data = {
                        "id": contract.id,
                        "legal_id": contract.legal_id,
                        "client": contract.client,
                        "event": contract.event
                        }
                    with sentry_sdk.push_scope() as scope:
                        scope.set_extra("contract_info", data)
                        sentry_sdk.capture_message('CONTRACT SIGNED', 'info')
                return contract
            except SQLAlchemyError:
                return SQLAlchemyError

    def delete(self, contract):
        with capture_exceptions():
            self.db_session.delete(contract)
            self.db_session.commit()
