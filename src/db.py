from pony.orm import db_session, commit
from src.models import db

from config import DB_USER, DB_NAME, DB_PASS, DB_HOST


class DBWorker(object):
    db = db
    provider = 'postgres'

    def __init__(self):
        self.db.bind(
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

    @db_session
    def bulk_create(self, model, data_lst):
        create_lst = []
        for data in data_lst:
            create_lst.append(model(**data))
        commit()

