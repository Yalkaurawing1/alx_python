"""a python file that contains the
class definition of a State and an
instance Base = declarative_base():
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# A class to create the tables
class State(Base):
    '''
    A class that models the table 'states', inherited from Base

    Attributes:

        id(int): unique identity number of each state

        name(string): name of each state
    '''
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
        