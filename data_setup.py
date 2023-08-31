
from models.base import Base
from database.db_session import engine
from models.client import Client
from models.collaborator import Collaborator
from models.contract import Contract
from models.event import Event
from models.role import Role
from database.db_session import session
from dao.client_dao import ClientDao
from dao.collaborator_dao import CollaboratorDao
from dao.contract_dao import ContractDao
from dao.event_dao import EventDao
from repository.client_repository import ClientRepository
from repository.collaborator_repository import CollaboratorRepository
from repository.contract_repository import ContractRepository
from repository.event_repository import EventRepository
from datetime import date
import argparse
from auth.auth_handler import AuthHandler


auth_handler = AuthHandler()

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
# Add arguments to the parser
parser.add_argument("--reset",
                    help="Has the data previously been set up",
                    default=False)
parser.add_argument("--add_demo_data",
                    help="Should the script add some demo data",
                    default=True)
# Parse the arguments
args = parser.parse_args()


# If the data preexist, drop the table first
if args.reset:
    # Drop tables if model changed
    Event.__table__.drop(engine)
    Contract.__table__.drop(engine)
    Client.__table__.drop(engine)
    Collaborator.__table__.drop(engine)
    Role.__table__.drop(engine)

# Create (or update) tables based on model definitions
Base.metadata.create_all(engine)

# Empty the tables
# session.query(Collaborator).delete()
# session.query(Client).delete()
# session.query(Contract).delete()
# session.query(Event).delete()
# session.commit()

# Instanciate DAOs
client_dao = ClientDao(session)
collaborator_dao = CollaboratorDao(session)
contract_dao = ContractDao(session)
event_dao = EventDao(session)

# Instanciate Repositories
client_repo = ClientRepository(client_dao)
collaborator_repo = CollaboratorRepository(collaborator_dao)
contract_repo = ContractRepository(contract_dao)
event_repo = EventRepository(event_dao)

# Populate initial data

admin_role = Role(
    name="Admin"
)
sales_role = Role(
    name="Sales"
)
support_role = Role(
    name="Support"
)
session.add(admin_role)
session.add(sales_role)
session.add(support_role)
session.commit()
first_admin = Collaborator(
    username="admin",
    password=auth_handler.hash_password("admin123"),
    name="Default",
    surname="Admin",
    email="admin@default.com",
    telephone="0000000000",
    role_id=admin_role.id
    )
session.add(first_admin)
session.commit()

if args.add_demo_data:
    first_collab = Collaborator(
        username="jeanbon",
        password=auth_handler.hash_password("123jean456"),
        name="Jean",
        surname="Bon",
        email="jean.bon@gmail.com",
        telephone="0612564321",
        role_id=sales_role.id
        )
    session.add(first_collab)
    session.commit()

    second_collab = Collaborator(
        username="jeannebon",
        password=auth_handler.hash_password("456jeanne123"),
        name="Jeanne",
        surname="Bon",
        email="jeanne.bon@gmail.com",
        telephone="0605102577",
        role_id=support_role.id
        )
    session.add(second_collab)
    session.commit()

    first_client = Client(
        name="Jean-Michel",
        surname="Clientelle",
        email="jm-clientelle@wanadoo.fr",
        telephone="0607050401",
        enterprise_name="Bellevie",
        create_date=date(2022, 5, 15),
        last_update_date=date(2023, 8, 9),
        contact_id=first_collab.id
        )
    session.add(first_client)
    session.commit()

    first_contract = Contract(
        legal_id='156A24B',
        price=1240.25,
        remaining_to_pay=220.25,
        create_date=date(2023, 5, 1),
        status="En cours",
        client_id=first_client.id
        )
    session.add(first_contract)
    session.commit()

    first_event = Event(
        title="Mariage super",
        start_date=date(2023, 9, 30),
        end_date=date(2023, 10, 2),
        location="Petaouchnok",
        attendees=234,
        comments="Ca va être chouette",
        support_id=second_collab.id,
        contract_id=first_contract.id
        )
    session.add(first_event)
    session.commit()
