#!/usr/bin/python3
"""
contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance of Base = declarative_base()
Base = declarative_base()


class State(Base):
    """
    class definition of a State
    table name is states and
    columns id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
