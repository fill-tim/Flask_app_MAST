from typing import Any
from ..core.db import connect_db
from ..models.data_model import DataCreate


class DataRepo:
    def __init__(self) -> None:
        self._conn = connect_db()
        self._cur = self._conn.cursor()

    def get_all(self) -> list[Any]:
        self._cur.execute("SELECT * FROM data")

        data = self._cur.fetchall()

        return data

    def create(self, data_create: DataCreate) -> DataCreate:
        self._cur.execute(
            "INSERT INTO data VALUES (?, ?, ?, ?)",
            (
                data_create.text,
                data_create.date,
                data_create.time,
                data_create.click_count,
            ),
        )

        self._conn.commit()

        return data_create
