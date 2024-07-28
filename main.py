from config import logger
from src.db import DBWorker
from src.services import clone_character_base


if __name__ == '__main__':
    db = DBWorker()
    while True:
        action = input(
            'Для старта загрузки введите любое значение, для выхода q\n')
        if action == 'q':
            break
        else:
            try:
                clone_character_base(db)
                logger.info("Данные успешно загружены\n")
            except Exception as e:
                logger.exception(e)
                logger.error("Не удалось получить данные\n")
