from hardcore_tracker import gw2_user, db_client, constants
# from hardcore_tracker.gw2_user import GW2_User
# from hardcore_tracker.db_client import GW2_Hardcore_Database_Client
# from hardcore_tracker.constants import TEST_API_KEY, TEST_USERNAME


def test_making_gw2_user_with_gw2_api():

    data = {"api_key": constants.TEST_USERNAME, "username": constants.TEST_USERNAME}
    my_user = gw2_user.GW2_User(**data)
    assert my_user.api_key == constants.TEST_API_KEY
    assert my_user.username == constants.TEST_USERNAME
    assert my_user.any_non_hardcore_characters() is True
    assert my_user.characters == [
                        "Sxcept",
                        "Alac Daddy",
                        "Pillow Engineer",
                        "X Ragnorak X",
                        "Solo Pillow",
                        "Short Pillow",
                        "Lonar Thick",
                        "Steal Pillow",
                        "Pillow Guard Dog"
    ]

def test_making_gw2_user_with_db_data():
    my_db = db_client.GW2_Hardcore_Database_Client()
    user_data = my_db.get_user(constants.TEST_USERNAME)
    my_user = gw2_user.GW2_User(**user_data)
    assert my_user.username == constants.TEST_USERNAME
    assert my_user.any_non_hardcore_characters() is True
    assert my_user.characters == [
                        "Sxcept",
                        "Alac Daddy",
                        "Pillow Engineer",
                        "X Ragnorak X",
                        "Solo Pillow",
                        "Short Pillow",
                        "Lonar Thick",
                        "Steal Pillow",
                        "Pillow Guard Dog"
    ]