import logging
import os

from dotenv import load_dotenv

env = load_dotenv()


# DataBase settings
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

# API settings
API_URL = os.getenv("API_URL")
API_CHARACTER_URL = os.getenv("API_CHARACTER_URL")

# logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|%(levelname)s|%(message)s'
)
logger = logging.getLogger()
