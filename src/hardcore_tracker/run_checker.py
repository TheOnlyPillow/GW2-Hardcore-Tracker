from hardcore_tracker.api_sheet import get_all_users
from hardcore_tracker.gw2_user import GW2_User


def main():
    all_users = get_all_users()
    for user in all_users:
        api_key = all_users.get(user)
        current_user = GW2_User(user, api_key)
        print(current_user.get_hardcore_characters())

def check_individual_user(username: str):
    pass


if __name__ == "__main__":
    main()