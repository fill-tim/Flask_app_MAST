import os
import sqlite3
from app import start_app
import pytest

app = start_app(db_url="test_data.db")


@pytest.fixture(autouse=True)
def reset_db():
    db_name = "test_data.db"

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("DELETE FROM data")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS data (text TEXT, date TEXT, time TEXT, click_count INTEGER)"
    )
    conn.commit()

    conn.close()


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def create_data_for_test():
    conn = sqlite3.connect("test_data.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO data VALUES (?, ?, ?, ?)",
        (
            "test_text",
            "Mon Feb 12 2024",
            "11:54:50",
            "1",
        ),
    )

    conn.commit()
    conn.close()
