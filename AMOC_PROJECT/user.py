import uuid
import datetime
from flask import session
from werkzeug.security import generate_pasword_hash, check_password_hash
from database import Database


class User(object):
    def __init__(self, email, hash_value, _id=None):
        self.email = email
        self.password = hash_value
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(users, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(users, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password, hash_value):  # validate the user
        user = User.get_by_email(email)
        if user is not None:
            # check password
            return check_password_hash(hash_value, password)
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:  # if it is not registered
			hash_value = generate_pasword_hash(password)
            new_user = users(email, hash_value)
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
