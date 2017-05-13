import uuid
import datetime
from flask import session

from common.database import Database


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("student", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):  # validate the user
        user = User.get_by_email(email)
        if user is not None:
            # check password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:  # if it is not registered
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        # login valid is already called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def save_to_mongo(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }
