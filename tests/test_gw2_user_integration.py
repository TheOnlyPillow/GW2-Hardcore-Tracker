from hardcore_tracker.gw2_user import GW2_User
from hardcore_tracker.db import GW2_Hardcore_Database_Client
from hardcore_tracker.data.constants import TEST_API_KEY, TEST_USERNAME


def test_making_gw2_user_with_gw2_api():

    data = {"api_key": TEST_USERNAME, "username": TEST_USERNAME}
    my_user = GW2_User(**data)
    assert my_user.api_key == TEST_API_KEY
    assert my_user.username == TEST_USERNAME
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
    my_db = GW2_Hardcore_Database_Client()
    user_data = my_db.get_user(TEST_USERNAME)
    my_user = GW2_User(**user_data)
    assert my_user.username == TEST_USERNAME
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