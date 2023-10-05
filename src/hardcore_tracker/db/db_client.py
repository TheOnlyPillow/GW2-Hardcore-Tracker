import pymongo
from hardcore_tracker.gw2_user import GW2_User
from data.constants import MONGODB_CONNECTION_URL, MONGODB_DB_NAME

class GW2_Hardcore_Database_Client:
    def __init__(self):
        self.connection_url = MONGODB_CONNECTION_URL
        self.database_name = MONGODB_DB_NAME

    def connect(self):
        self.client = pymongo.MongoClient(self.connection_url)
        self.db = self.client[self.database_name]

    def disconnect(self):
        self.client.close()

    def insert_user(self, user: GW2_User) -> None:
        """
        Inserts a user into the MongoDB collection "users" with all the GW2_User data
        jsonified
        """
        try:
            self.connect()
            collection = self.db["Users"]
            if self.check_if_username_exists(user.username):
                print("User already exists in database.")
            else:
                collection.insert_one(user.__dict__)
        finally:
            self.disconnect()

    def check_if_username_exists(self, username: str) -> bool:
        """
        Checks to see if the user already exists in the database by checking for the username
        """
        try:
            self.connect()
            collection = self.db["Users"]
            collection
            if collection.find_one({"username": username}):
                return True
            return False
        finally:
            self.disconnect()

    def update_user(self, user: GW2_User):
        """
        Updates a user in the database with the new data from the GW2_User object passed in.
        The user must already exist in the database.
        The GW2_User object must have the username set to the username of the user that is being updated.
        """
        try:
            self.connect()
            collection = self.db["Users"]
            collection.update({"username": user.username}, user.toJSON())
        finally:
            self.disconnect()

    def get_user_data(self, username: str):
        """
        Gets a user from the database by their username if it exists, then creates a GW2_User Object from this.
        If it does not exist, return None
        """
        try:
            self.connect()
            collection = self.db["Users"]
            user_data = collection.find_one({"username": username})
            if user_data:
                user = GW2_User(user_data)
                return user
            return None
        finally:
            self.disconnect()