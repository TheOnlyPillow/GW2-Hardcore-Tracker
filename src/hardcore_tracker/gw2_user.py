import requests
import json

class GW2_User:
    
    def __init__(self, **user_information):
        """
        Creates a new GW2_User object.
        """
        if not user_information:
            raise ValueError("User information is required")
        if not user_information.get("username") and not user_information.get("api_key"):
            raise ValueError("Username and API key are required")
        
        self.username = user_information.get("username")
        self.api_key = user_information.get("api_key")
        self.characters = user_information.get("characters", [])
        self.characters_info = user_information.get("characters_info", {})
        self.hardcore_characters = user_information.get("hardcore_characters", [])
        self.get_characters()
        self.get_characters_info()

    def get_characters(self):
        """
        Gets all of the character usernames from this object's API key and stores it in the 
        object's characters variable
        """
        character_endpoint = f"https://api.guildwars2.com/v2/characters/?access_token={self.api_key}"
        character_request = requests.get(character_endpoint)
        if character_request.status_code != 200:
            print(f"Unable to get characters for user: {self.username}")
            self.characters = []
        else: 
            self.characters = character_request.json()

    def get_characters_info(self):
        """
        Gets all of the character info from the GW2 API endpoint. Then stores that into the
        object's characters_info variable
        """
        self.characters_info = {}
        self.hardcore_characters = []
        if self.characters:
            for character in self.characters:
                character_info_endpoint = f"https://api.guildwars2.com/v2/characters/{character}/core?access_token={self.api_key}"
                character_info = requests.get(character_info_endpoint).json()
                self.characters_info[character] = character_info
                self.update_hardcore_character_list(character)
    
    def update_hardcore_character_list(self, character: str) -> None:
        """
        Updates the object's hardcore character list by checking the current character's information
        to see if it has any deaths. If the character has no deaths, the character is considered hardcore. 
        """
        character_death_count = self.characters_info.get(character)['deaths']
        if character_death_count == 0:
            self.hardcore_characters.append(character)
        elif character_death_count > 0 and character in self.hardcore_characters:
            self.hardcore_characters.remove(character)

    def get_hardcore_characters(self) -> list:
        """
        Returns the list of hardcore characters for this user. This list is updated every time
        the get_characters_info() function is called. 
        """
        return self.hardcore_characters

    def any_non_hardcore_characters(self) -> bool:
        """
        Returns a boolean value based on whether or not there are more non-hardcore characters than
        there are hardcore characters.
        """
        num_hardcore_characters = len(self.hardcore_characters)
        return num_hardcore_characters < len(self.characters)

    def toJSON(self) -> dict:
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)
