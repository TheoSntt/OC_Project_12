from models.contract import Contract


class ContractDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_by_id(self, contract_id):
        return self.db_session.get(Contract, contract_id)

    def get_by_expression(self, expression):
        return self.db_session.query(Contract).filter(expression).all()

    def create(self, contract):
        self.db_session.add(contract)
        self.db_session.commit()

    def update(self, contract):
        self.db_session.commit()

    def delete(self, contract):
        self.db_session.delete(contract)
        self.db_session.commit()
