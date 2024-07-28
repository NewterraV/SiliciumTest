from src.api import APIGetter
from src.db import DBWorker
from src.models import Character


def clone_character_base(db):
    api = APIGetter()
    character_data_lst = api.get_characters()
    db.bulk_create(Character, character_data_lst, 'url')
