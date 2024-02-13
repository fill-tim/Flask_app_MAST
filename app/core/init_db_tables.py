from ..core.db import connect_db


def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS data (text TEXT, date TEXT, time TEXT, click_count INTEGER)"
    )

    conn.commit()
