import json

from pony.orm import Database, db_session, commit, Required, Optional, Json

from config import DB_USER, DB_NAME, DB_PASS, DB_HOST

db = Database()

class Character(db.Entity):
    name = Required(str)
    height = Optional(int)
    mass = Optional(int)
    hair_color = Optional(str)
    skin_color = Optional(str)
    eye_color = Optional(str)
    birth_year = Optional(str)
    gender = Optional(str)
    home_world = Required(str, unique=True)
    films = Required(Json)
    species = Required(Json)
    vehicles = Optional(Json)
    starships = Optional(Json)
    created = Required(str)
    edited = Required(str)
    url = Required(str, unique=True)


class DBWorker(object):
    db = db
    provider = 'postgres'

    def __init__(self):
        db.bind(
            provider='postgres',
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME,
        )
        self.db.generate_mapping(create_tables=True)

    @db_session
    def create_instance(self, model, **kwargs):
        instance = model(**kwargs)
        commit()
        return instance.id

