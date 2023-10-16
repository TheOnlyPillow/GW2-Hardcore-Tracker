from db_client import GW2_Hardcore_Database_Client
from gw2_user import GW2_User

from constants import TEST_API_KEY, TEST_USERNAME

print("Getting user from gw2 api")
my_user = GW2_User(**{"api_key": TEST_API_KEY, "username": TEST_USERNAME})

print("Inserting user into database")
db_client = GW2_Hardcore_Database_Client()
db_client.insert_user(my_user)

print("Done")