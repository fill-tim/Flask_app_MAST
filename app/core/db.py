import sqlite3
from ..core.config import config


def connect_db():
    try:
        db_url = config.db_url
        
        conn = sqlite3.connect(db_url, check_same_thread=False)

        return conn
    except Exception as error:
        print(error)
