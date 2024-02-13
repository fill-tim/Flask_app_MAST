from typing import Literal
from flask import Response, jsonify
from ..repositories.data_repo import DataRepo
from ..models.data_model import DataCreate


class DataService:
    def __init__(self):
        self._data_repo = DataRepo()

    def get_all_data(self) -> tuple[list, Literal[200]] | tuple[str, Literal[400]]:
        try:
            data: list[str | int] = self._data_repo.get_all()

            response: list = []

            for item in data:
                response.append(
                    {
                        "text": item[0],
                        "date": item[1],
                        "time": item[2],
                        "click_count": item[3],
                    }
                )

            return jsonify(response), 200
        except Exception as error:
            return str(error), 400

    def add_data(
        self, data_in: dict[str | int]
    ) -> tuple[str, Literal[400]] | tuple[dict, Literal[200]]:
        try:
            data_create: DataCreate = DataCreate(**data_in)

            if data_create.text == "":
                return jsonify({"detail": "Введите текст в поле ввода!"}), 400

            data: DataCreate = self._data_repo.create(data_create=data_create)

            return (
                jsonify(
                    {
                        "text": data.text,
                        "date": data.date,
                        "time": data.time,
                        "click_count": data.click_count,
                    }
                ),
                201,
            )
        except Exception as error:
            return str(error), 400
