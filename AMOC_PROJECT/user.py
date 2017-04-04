import uuid
import datetime
from flask import session
# from werkzeug.security import generate_pasword_hash, check_password_hash
from database import Database


class User(object):
    def __init__(self, email, username, cid, mob = None, hname = None, rnum = None,photolink = None, _id=None):
        self.email = email
        self.password = password
	self.username = username
	self.cid = cid
	self.mob = mob
	self.hname = hname
	self.photolink = photolink
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(users, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

	@classmethod
    def get_by_username(users, username):
        data = Database.find_one("users", {"username": username})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_cid(users, cid):
        data = Database.find_one("users", {"cid": cid})
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
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password, cid, mob, hname, rnum, photolink):
        user = cls.get_by_email(email)
        if user is None:# if it is not registered
	    	# hash_value = generate_pasword_hash(password)
            new_user = cls(email, password, cid, mob, hname, rnum, photolink)
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
            "password": self.password,
		"username":self.username
	    "cid": self.cid,
	    "mob": self.mob,
	    "hanme": self.hname,
	    "rnum": self.rnum,
	    "photolink": self.photolink
        }
