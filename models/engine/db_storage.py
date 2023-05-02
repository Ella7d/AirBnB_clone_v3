#!/usr/bin/python3
"""Module for DBstorage class"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
         """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns all objects of cls"""
        d = {}
        if cls is None:
            for c in self.all_classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    d[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                d[key] = instance
        return d

    def new(self, obj):
        """add object to db"""
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database """
        Base.metadata.create_all(self.__engine)
        sessionf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionf)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
         def get(self, cls, id):
        """ Retrieves one object """
        objects = list(self.all(cls).values())
        for object in objects:
            if object.id == id:
                return (object)

    def count(self, cls=None):
        """ Counts the number of objects in storage """
        objects = list(self.all(cls).values())
        return(len(objects))
