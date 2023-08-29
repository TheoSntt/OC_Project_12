from models.contract import Contract
from sqlalchemy import and_
from dao.sanitize_input import sanitize_input


class ContractDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, contract_id):
        return self.db_session.get(Contract, contract_id)

    def get_all(self):
        return self.db_session.query(Contract).all()

    def get_by_expression(self, filters):
        filter_conditions = []
        for field, value in filters.items():
            column = getattr(Contract, field, None)
            if column is not None:
                filter_conditions.append(column == sanitize_input(value))
        # Combine the filter conditions using the 'and_' function
        combined_filter = and_(*filter_conditions)
        return self.db_session.query(Contract).filter(combined_filter)

    def create(self, contract):
        self.db_session.add(contract)
        self.db_session.commit()

    def update(self, contract):
        self.db_session.commit()

    def delete(self, contract):
        self.db_session.delete(contract)
        self.db_session.commit()
