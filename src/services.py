from src.api import APIGetter
from src.db import DBWorker


def clone_character_base():
    character_id = 0
    character_data_lst = []
    db = DBWorker()
    api = APIGetter()
    while True:
        character_id += 1
        character_data = api.get_character(character_id)
        if character_data:
            character_data_lst.append(character_data)
        else:
            break
    db.bulk_create(character_data_lst)
