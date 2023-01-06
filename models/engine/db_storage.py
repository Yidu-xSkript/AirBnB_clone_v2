#!/usr/bin/python3
"""DB Storage"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Database Storage as an alternative from file storage
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                    format(getenv("HBNB_MYSQL_USER"),
                                            getenv("HBNB_MYSQL_PWD"),
                                            getenv("HBNB_MYSQL_HOST"),
                                            getenv("HBNB_MYSQL_DB")),
                                    pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, _class=None):
        """Queries all database object

        Args:
            _class (_type_, optional): _description_. Defaults to None.
        """

        if _class is None:
            allObj = self.__session.query(State).all()
            allObj.extend(self.__session.query(City).all())
            allObj.extend(self.__session.query(User).all())
            allObj.extend(self.__session.query(Place).all())
            allObj.extend(self.__session.query(Amenity).all())
            allObj.extend(self.__session.query(Review).all())
        else:
            if type(_class) == str:
                _class = eval(_class)
            allObj = self.__session.query(_class)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in allObj}

    def new(self, obj):
        """Add obj to the db."""
        self.__session.add(obj)

    def save(self):
        """Save changes to db."""
        self.__session.commit()

    def delete(self, obj=None):
        """destroy obj from db."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload session and db."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()