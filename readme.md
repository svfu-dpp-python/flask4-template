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

1. Добавьте шаблон страницы аутентификации `login.html`:

```html
{% extends 'base.html' %}

{% block content %}
<h1>Вход на сайт</h1>
<form method="post">

    <div class="row">
        <label>Логин</label>
        <input type="text" name="username" value="{{ username }}">
    </div>

    <div class="row">
        <label>Пароль</label>
        <input type="password" name="password">
    </div>

    <div class="row">
        <input type="submit" value="Войти">
        <a href="{{ url_for('index_page') }}">Отмена</a>
    </div>
</form>
{% endblock %}
```

2. Добавьте функцию `login_page()`:

```python
def login_page():
    username = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "pass":
            session["username"] = username
            return redirect(url_for("index_page"))
    return render_template("login.html", username=username)
```

3. Добавьте функцию `logout()`:

```python
def logout():
    session.pop("username")
    return redirect(url_for("index_page"))
```

4. Добавьте секретный ключ (для шифрования данных сессии) в `create_app()`:

```python
app.config["SECRET_KEY"] = "secret"
```

5. Добавьте соответствующие правила для URL в `create_app()`:

```python
app.add_url_rule("/login/", view_func=views.login_page, methods=["GET", "POST"])
app.add_url_rule("/logout/", view_func=views.logout)
```

6. Добавьте в шаблон `index.html` навигационную панель перед заголовком:

```html
<div class="menu">
    {% if 'username' in session %}
    <span>{{ session['username'] }}</span>
    <a href="{{ url_for('logout') }}">Выход</a>
    {% else %}
    <a href="{{ url_for('login_page') }}">Вход</a>
    {% endif %}
</div>
```

7. Проверьте работу механизма аутентификации

8. Удалите Cookie и проверьте что это приводит к очистке данных сессии:

![Очистка Cookie](img/cookie.png)

9. Сделайте коммит

## Создание админки

1. Добавьте таблицу с данными студентами:

```python
class Student(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30))
```

2. Добавьте админку в `create_app()`:

```python
admin = Admin(app)
admin.add_link(MenuLink(name='Главная', url="/"))
admin.add_view(ModelView(models.Student, db.session))
```

и соответствующие импорты

```python
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
```

3. Добавьте ссылку на админку в меню рядом с именем вошедшего пользователя:

```html
<a href="{{ url_for('admin.index') }}">Админка</a>
```

4. Проверьте работу админки

5. Сделайте коммит

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
