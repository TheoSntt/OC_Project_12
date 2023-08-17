from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import os


# Create a configparser object and read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Read the values from the [mysql] section
username = os.environ.get("MYSQL_PROJECT_USERNAME")
password = os.environ.get("MYSQL_PROJECT_PW")
host = config['mysql']['host']
port = config['mysql']['port']
dbname = config['mysql']['dbname']

# Creating the SQLAlchemy engine
connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{dbname}"
engine = create_engine(connection_string, echo=False)
# Creating the SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()
