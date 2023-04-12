# Flask-4

## Предварительные шаги

1. Откройте каталог проекта в редакторе VS Code

2. Создайте и активируйте виртуальное окружение 

Powershell:

```powershell
py -m venv venv
venv\scripts\activate.ps1
```

Командная строка:

```cmd
py -m venv venv
venv\scripts\activate.bat
```

3. Установите библиотеки используя список из `requirements.txt`:

```powershell
pip install -r requirements.txt
```

4. Инициализируйте базу данных:

```powershell
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Разрешите отладку и запустите веб-сервер разработчика:

Powershell:

```powershell
$ENV:FLASK_DEBUG=1
flask run
```

Командная строка:

```cmd
set FLASK_DEBUG=1
flask run
```

## Сессии

1. Добавьте страницу аутентификации

Добавьте шаблон `login.html`:

Добавьте функцию `login_page()`:

Добавьте секретный ключ (для шифрования данных сессии) в `create_app()`:

Добавьте соответствующее правило для URL в `create_app()`.

Добавьте в базовый шаблон навигационную панель

2. Проверьте работу механизма аутентификации

3. Проверьте что удаление Cookie приводит к очистке данных сессии

4. Сделайте коммит

## Проверка данных и обработка ошибок

Исправьте страницу аутентификации.

Проверьте работу.

Сделайте коммит.

## Создание админки

Установите расширение `Flask-Admin`.

Добавьте ссылку на админку.

Проверьте работу.

Сделайте коммит.

## Создание связей между таблицами

Создайте новую таблицу .

Проверьте работу.

Сделайте коммит.

## Ссылки

* [Документация Flask](https://flask.palletsprojects.com/)
* [Документация Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [Документация Flask-Migrate](https://flask.palletsprojects.com/)
* [Документация Flask-Admin](https://flask-admin.readthedocs.io/)
* [Документация SqlAlchemy](https://www.sqlalchemy.org/)
* [Документация Alembic](https://alembic.sqlalchemy.org/)
