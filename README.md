# API Final Yatube
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/EvgVol)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)

## Описание проекта api_final_yatube
Проект api_final_yatube является версией 2.0 проекта [api_yatube](https://github.com/EvgVol/api_yatube). В проекте описана новая модель Follow, в которой два поля — user (кто подписан) и following (на кого подписан). Для этой модели описан эндпоинт /follow/ и два метода:
GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру search
POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь получает информативное сообщение об ошибке. Проверка осуществляется на уровне API.
Анонимный пользователь на запросы к этому эндпоинту получает ответ с кодом 401 Unauthorized.


## Используемые технологии
- Python 3.7.9
- Django REST Framework
- API REST
- Postman
- SQLite3
- Simple-JWT

## Подготовка к запуску и запуск проекта api_final_yatube
Клонирование репозитория:

```
git clone git@github.com:ваш-аккаунт-на-гитхабе/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate 
```

```
python -3.7 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнение миграций:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver

```
## Документация

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube

