#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    @property
    def cities(self):
        """  getter attribute cities that returns the list of
        City instances with state_id equals to the current State.id """
        from models import storage
        allcities = storage.all(City)
        c = []
        for k, v in allcities.items():
            if v.state_id == self.id:
                c.append(v)
        return c
