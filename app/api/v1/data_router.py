from typing import Literal
from flask import request
from ...services.data_service import DataService
from flask.views import MethodView


class Data(MethodView):
    def __init__(self) -> None:
        self._data_service = DataService()

    def post(self) -> tuple[dict, Literal[201]] | tuple[str, Literal[400]]:
        data_in: dict[str | int] = request.get_json()

        return self._data_service.add_data(data_in=data_in)

    def get(self) -> tuple[list, Literal[200]] | tuple[str, Literal[400]]:
        return self._data_service.get_all_data()


data = Data.as_view(name="data_api")
