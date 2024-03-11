#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base

env = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if env == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete-orphan"
            )
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            city_list = []
            for key in storage.all("City"):
                if storage.all("City")[key].state_id == self.id:
                    city_list.append(storage.all("City")[key])
            return city_list
