import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.contract import Contract
from models.role import Role


# Define a custom Pytest fixture to set up the database
@pytest.fixture(scope="module")
def test_db():
    # Use an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')

    # Create tables in the temporary database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Yield the session to the test functions
    yield session

    # Clean up: close the session and drop tables
    session.close()
    Base.metadata.drop_all(engine)


# Define a test case to check the unique constraint on legal_id
def test_unique_legal_id(test_db):
    # Create two Contract instances with the same legal_id
    contract1 = Contract(legal_id="ABC123", price=1000.0, remaining_to_pay=800.0, status="Active")
    contract2 = Contract(legal_id="ABC123", price=1200.0, remaining_to_pay=1000.0, status="Inactive")

    # Add the first contract to the database
    test_db.add(contract1)
    test_db.commit()

    # Attempt to add the second contract with the same legal_id
    with pytest.raises(exc.IntegrityError):
        test_db.add(contract2)
        test_db.commit()

# Run the tests using `pytest`
