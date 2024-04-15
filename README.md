# QRKot - API для проекта по краудфандингу котиков
### Сервис QRKot позволяет отправлять пожертвования и создавать проект для сбора средств, а также получать отчеты в виде гугл таблиц.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустите приложение командой:
```
uvicorn app.main:app
```

Примеры запросов:
/donation/
```
{
  "full_amount": 10000,
  "comment": "string"
}
result:
{
  "full_amount": 10000,
  "comment": "string",
  "id": 15,
  "create_date": "2024-04-09T22:07:56.894736"
}
```
/charity_project/
```
{
  "name": "new",
  "description": "123",
  "full_amount": 50000
}
result:
{
  "name": "new",
  "description": "123",
  "full_amount": 50000,
  "id": 30,
  "invested_amount": 0,
  "fully_invested": false,
  "create_date": "2024-04-09T22:07:46.255588"
}
```
### Стек: FastAPI, SQLAlchemy, Alembic, asyncio, SQLite, aiogoogle, googleapi

# Автор: mitsushidu