#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

env = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """
    This class inherits from BaseModel and SQLAlchemy's declarative base,
    providing a structure for storing user data in a database.
    """
    # Define the name of the table in the database
    __tablename__ = 'users'
    if env == 'db':
        # Define the email column, cannot be null
        email = Column(String(128), nullable=False)
        # Define the password column, cannot be null
        password = Column(String(128), nullable=False)
        # Define the first_name column, and can be null
        first_name = Column(String(128), nullable=True)
        # Define the last_name column, and can be null
        last_name = Column(String(128), nullable=True)
        # Define the relationship with Place objects
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
