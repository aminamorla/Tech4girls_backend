from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create base class for our classes to inherit from
Base = declarative_base()

# Define the Backend class
#class Backend(Base):
# models.py

class MyLaptops:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
        

    __tablename__ = 'backend_class'  # Corrected the typo here

    # Columns for the table
    student_id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(256), nullable=False, unique=True)

    # Define string representation method for easy printing
    def __str__(self):
        return f"Student's ID: {self.student_id}, Name: {self.firstname} {self.lastname}, Age: {self.age}, Email: {self.email}."

# Create an SQLite database engine (or connect to one)
DATABASE_URL = 'sqlite:///students.db'  # Example SQLite database URL
engine = create_engine(DATABASE_URL)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Code to create all tables in the database
if __name__ == '__main__':
    try:
        # Create all tables in the database
        Base.metadata.create_all(engine)
        print('Tables created successfully.')

    except Exception as e:
        print(f'An error occurred: {e}.')
