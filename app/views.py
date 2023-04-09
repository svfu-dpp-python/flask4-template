"""
Функции представления
"""
from flask import render_template


def index_page():
    """
    Главная страница сайта
    """
    return render_template("index.html")
