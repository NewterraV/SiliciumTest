from pony.orm import Database, Required, Optional, Json

db = Database()

class Character(db.Entity):
    name = Required(str)
    height = Optional(str)
    mass = Optional(str)
    hair_color = Optional(str)
    skin_color = Optional(str)
    eye_color = Optional(str)
    birth_year = Optional(str)
    gender = Optional(str)
    homeworld = Required(str)
    films = Required(Json)
    species = Required(Json)
    vehicles = Optional(Json)
    starships = Optional(Json)
    created = Required(str)
    edited = Required(str)
    url = Required(str, unique=True)
