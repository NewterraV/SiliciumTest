from pony.orm import db_session, commit
from src.models import db

from config import DB_USER, DB_NAME, DB_PASS, DB_HOST
from config import logger


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
    def bulk_create(self, model, data_lst, unique_field_name: None):
        create_lst = []
        update_lst = []
        for data in data_lst:
            if unique_field_name:
                instance = model.get(
                    **{unique_field_name: data.get(unique_field_name)})
                if instance:
                    instance.set(**data)
                    update_lst.append(instance)
                    continue
            create_lst.append(model(**data))
        commit()
        logger.info(
            f'\nCreated instance: {len(create_lst)}\n'
            f'Updated instance: {len(update_lst)}')
