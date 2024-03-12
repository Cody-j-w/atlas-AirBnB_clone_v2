#!/usr/bin/python3

"""
Module containing HBnB Console's Database engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base

mydb = "mysql+mysqldb"
usr = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
environment = getenv("HBNB_ENV")
connect = '{0}://{1}:{2}@{3}:3306/{4}'.format(mydb, usr, pwd, host, db)
db_metadata = MetaData()

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    Engine for the console's database connection
    Attributes:
        __engine: the DB connection engine
        __session: the current DB session
    """

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(connect, pool_pre_ping=True)
        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        self.__session.close()
        self.reload()
