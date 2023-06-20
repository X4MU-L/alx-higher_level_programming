#!/usr/bin/python3
"""Creates a state object mapper"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Object class cities

    __tablename__ (string): the neme of the table instance
    id (int): auto generated integer, not null, primay key of table
    name (string): the name of the city
    state_id (int): foreign key, state id of the city
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
