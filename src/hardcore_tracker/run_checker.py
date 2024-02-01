from api_sheet import get_all_users
from gw2_user import GW2_User
from db_client import GW2_Hardcore_Database_Client

def update_database():
    all_users = get_all_users()
    db_client = GW2_Hardcore_Database_Client()
    for user in all_users:
        api_key = all_users.get(user)
        user_info = {"username": user,"api_key":api_key}
        current_user = GW2_User(**user_info)
        db_client.add_user(current_user)

def main():
    update_database()


def check_individual_user(username: str):
    db_client = GW2_Hardcore_Database_Client()
    user_data = db_client.get_user_data(username)
    if user_data:
        print(user_data.hardcore_characters)
    else:
        print(f"{username} not found in DB.")

def check_for_character(character_name: str):
    db_client = GW2_Hardcore_Database_Client()
    user_data = db_client.find_character(character_name)
    return user_data

if __name__ == "__main__":
    main()