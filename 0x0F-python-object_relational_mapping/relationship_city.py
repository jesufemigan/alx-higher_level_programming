#!/usr/bin/python3
'''a module that defines city class'''

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    '''a city class that inherits from base'''
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
