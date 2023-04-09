"""
Заголовок пакета
"""
from flask import Flask

from .database import db, migrate
from . import views


def create_app():
    """
    Создание приложения Flask
    """
    app = Flask(__name__)

    # База данных
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    migrate.init_app(app, db)

    # Функции представления
    app.add_url_rule("/", view_func=views.index_page)

    return app
