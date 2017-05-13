import uuid
from database import Database


class Guide(object):
    def __init__(self, uname, subject,_id=None):
        self.uname = uname
        self.subject = subject
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):  # these are methods this is for storing date
        Database.insert(collection='guide',
                        data=self.json())

    @classmethod
    def register(cls, uname, subject):
        new_user = cls(uname, subject)
        data = Database.find_one("guide", {"uname": uname})
        if data is None:
            new_user.save_to_mongo()

    @classmethod
    def get_by_uname(cls, uname):
        data = Database.find_one("guide", {"uname": uname})
        if data is None:
            return -1
        return cls(**data)

    def json(self):
        return {
            "uname": self.uname,
            "subject": self.subject,
            "_id":self._id
        }
