#!/usr/bin/python3
"""Creates a state object mapper"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Object class state

    __tablename__ (string): the neme of the table instance
    id (int): auto generated integer, not null, primay key of table
    name (string): the name of the state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
