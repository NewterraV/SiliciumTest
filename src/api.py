import requests

from config import API_URL, API_CHARACTER_URL


class APIGetter:
    base_url = API_URL

    def get_character(self, character_id):
        method = API_CHARACTER_URL.format(character_id)
        url = self.base_url + method
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
