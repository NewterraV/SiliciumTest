from time import sleep

import requests

from config import API_URL, API_CHARACTER_URL, logger


class APIGetter:
    base_url = API_URL

    def get_characters(self):
        method = API_CHARACTER_URL
        url = self.base_url + method
        all_characters = []
        while True:
            response = requests.get(url)
            logger.info(
                f'Getting characters from {url}. '
                f'status code: {response.status_code}'
            )
            if response.status_code == 200:
                characters = response.json().get('results')
                if characters:
                    all_characters.extend(characters)
                if response.json().get('next'):
                    url = response.json().get('next')
                else:
                    return all_characters
            else:
                return all_characters
