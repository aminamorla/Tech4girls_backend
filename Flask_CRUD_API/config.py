from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string
connection_str = 'mysql+mysqlconnector://yarauta:amina@localhost/tech4girls'

# Create an engine that knows how to connect to the database
engine = create_engine(connection_str)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

try:
    # Try to establish a connection and print status
    connection = engine.connect()
    print('Located and connected to database')
    connection.close()
except Exception as e:
    print(f'An error occurred: {e}')
