from flask import Flask

from .api.v1.data_router import data
from .core.init_db_tables import create_tables
from .core.config import config


def start_app(db_url: str = "data.db"):
    app = Flask(__name__)

    config.db_url = db_url
    create_tables()

    app.add_url_rule("/api/v1/data", view_func=data, methods=["GET"])
    app.add_url_rule("/api/v1/data", view_func=data, methods=["POST"])

    return app
