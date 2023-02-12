# api_final

## Автор:
Андрей [Ostashev](https://github.com/Ostashev) Осташев


## Описание:
api final - это REST API для блог-платформы Yatube. Позволяет просматривать и отправлять посты, просматривать группы, подписываться на авторов.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Ostashev/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

```
source venv/bin/activate 
```

Установить зависимости из файла requirements.txt:

```
python3.9 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в директорию yatube_api:

```
cd yatube_api
```

Выполнить миграции:

```
python3.9 manage.py migrate
```

Запустить проект:

```
python3.9 manage.py runserver
```
## Примеры запросов:
### Создание пользователя Name:
```
 [POST].../api/v1/users/
{
    "username": "Name",
    "password": "Changeme!"
}
```
### Ответ:
```
{
    "email": "",
    "username": "Name",
    "id": 3
}
```

### Запрос JWT токена с использованием логина и пароля пользователя Name:
```
 [POST].../api/v1/jwt/create/
{
    "username": "Name",
    "password": "Changeme!"
}
```
### Ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NjMwNTEwNiwianRpIjoiMGI1ZTMxMzYyYWNlNDU3YjhiNzI1NTMxNzExYjY5MDUiLCJ1c2VyX2lkIjozfQ._uWQAfVR4sK9R38iRFuBFN63Ey-HdtuWg1SKp3LHzec",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2MzA1MTA2LCJqdGkiOiIyNDU1YWZmMDhjODg0ZmQ2OTlmMDQ0MDdmYTJlMjA1ZCIsInVzZXJfaWQiOjN9.-C0Wneq3Lkp33rZY5zL0RYApAhcFbW8oopezZMBaSFk"
}
```
### Создание поста пользователем Name:
```
 [POST].../api/v1/posts/
{
"text": "Тестовый пост 1",
"group": 1
}
```

### Ответ:
```
{
    "id": 5,
    "text": "Тестовый пост 1",
    "author": "Name",
    "image": null,
    "group": 1,
    "pub_date": "2023-02-12T16:36:46.602702Z"
}
```
### Просмотр групп анонимным пользователем:
```
    [GET].../api/v1/groups/
```
### Ответ:
```
[
    {
        "id": 1,
        "title": "Группа 1",
        "slug": "group_1",
        "description": "Группа 1"
    },
    {
        "id": 2,
        "title": "Группа 2",
        "slug": "group_2",
        "description": "Группа 2"
    },
    {
        "id": 3,
        "title": "Группа 3",
        "slug": "group_3",
        "description": "Группа 3"
    }
]
```
### Добавление комментария к посту №1 пользователем Name:
```
    [GET].../api/v1/posts/1/comments/
{
    "text": "Тестовый комментарий 1"
}
```
### Ответ:
```
{
    "id": 1,
    "author": "Name",
    "text": "Тестовый комментарий 1",
    "created": "2023-02-12T16:43:04.245926Z",
    "post": 1
}
```

### Подробная документация в формате ReDoc доступна по адресу .../redoc/
