from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser


# Create a configparser object and read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Read the values from the [mysql] section
username = config['mysql']['username']
password = config['mysql']['password']
host = config['mysql']['host']
port = config['mysql']['port']
dbname = config['mysql']['dbname']

# Creating the SQLAlchemy engine
connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{dbname}"
engine = create_engine(connection_string, echo=True)
# Creating the SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()
