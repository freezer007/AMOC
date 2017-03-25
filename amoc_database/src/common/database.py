import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # def __init__(self):
    #   self.uri = ""
    #   self.database = None
    @staticmethod  # to tell we are not using self
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['amoc']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
