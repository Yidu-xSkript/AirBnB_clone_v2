#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            """Get a list of all related City objects."""
            _cities = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    _cities.append(city)
            return _cities
