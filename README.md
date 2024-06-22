# QRKot - API для проекта по краудфандингу котиков
## Сервис QRKot позволяет отправлять пожертвования и создавать проект для сбора средств, а также получать отчеты в виде гугл таблиц.
Реализованный функционал: создание, редактирование, удаление и получение проектов, отправка пожертвований и получение информации о них, регистрация и авторизация пользователей. Также есть возможность вывести информацию о закрытых проектах в google таблицу.

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

    ```bash
    git clone git@github.com:Mitsushidu/QRkot_spreadsheets.git
    cd QRkot_spreadsheets
    ```
2. Cоздать и активировать виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/scripts/activate
    ```
3. Установить зависимости из файла requirements.txt:

    ```bash
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
3. Заполнить файл .env:
    ```
    DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
    SECRET=POOPENSHTAUFEN
    ```

    Получить JSON-файл с ключом доступа к сервисному аккаунту на Google Cloud Platform. Перенести информацию из этого файла в .env:

    ```
    TYPE=
    PROJECT_ID=
    PRIVATE_KEY_ID=
    PRIVATE_KEY=
    CLIENT_EMAIL=
    CLIENT_ID=
    AUTH_URI=
    TOKEN_URI=
    AUTH_PROVIDER_X509_CERT_URL=
    CLIENT_X509_CERT_URL=
    ```
4. Применить миграции для таблиц:

    ```bash
    alembic upgrade head
    ```
5. Запустите приложение командой:

    ```bash
    uvicorn app.main:app
    ```

### Примеры запросов:
1. **Эндпоинт: http://127.0.0.1:8000/auth/register. 
    <br>Метод запроса: POST
    <br>Права доступа: доступно без токена**

    Запрос:

    * "email": "user@example.com" (required),
    * "password": "string" (required)
   
    Ответ:
  
    * "id": 1,
    * "email": "user@example.com" (required),
    * "is_active": true,
    * "is_superuser": false,
    * "is_verified": false

<br>

2. **Эндпоинт: http://127.0.0.1:8000/users/me. 
  <br>Метод запроса: GET
  <br>Права доступа: авторизованный пользователь** 

    Ответ:

    * "id": 1,
    * "email": "user@example.com" (required),
    * "is_active": true,
    * "is_superuser": false,
    * "is_verified": false

<br>

3. **Эндпоинт: http://127.0.0.1:8000/charity_project. 
<br>Метод запроса: GET
<br>Права доступа: доступно без токена**

    В ответ вы получите список всех благотворительных проектов.

<br>

4. **Эндпоинт: http://127.0.0.1:8000/charity_project. 
<br>Метод запроса: POST
<br>Права доступа: администратор**

    Запрос:

    * "name": "string" (required),
    * "description": "string" (required),
    * "full_amount": 100 (required)

    Ответ:

    * "name": "string" (required),
    * "description": "string" (required),
    * "full_amount": 100 (required),
    * "id": 1 (required),
    * "invested_amount": 0 (required),
    * "fully_invested": false (required),
    * "create_date": "2024-03-16T14:15:22Z" (required),
    * "close_date": null

    На счет проекта тут же поступят все свободные пожертвования(при их наличии).

<br>

5. **Эндпоинт: http://127.0.0.1:8000/donation. 
<br>Метод запроса: POST
<br>Права доступа: авторизованный пользователь**

    Запрос:

    * "full_amount": 100 (required),
    * "comment": "string"

    Ответ:

    * "full_amount": 100 (required),
    * "comment": "string",
    * "id": 1 (required),
    * "create_date": "2024-03-16T14:15:22Z" (required)

    Сумма запишется на счёт первого открытого проекта, если он существует.

<br>

6. **Эндпоинт: http://127.0.0.1:8000/donation. 
<br>Метод запроса: GET
<br>Права доступа: авторизованный пользователь**

    В ответ вы получите список всех пожертвований текущего пользователя.

<br>

7. **Эндпоинт: http://127.0.0.1:8000/google. 
<br>Метод запроса: POST
<br>Права доступа: администратор**

    В ответ вы получите список закрытых проектов, отсортированных по возрастанию времени сбора средств. О каждом будет представлена следующая информация:

    * "name": "string" (required),
    * "collection_time": "10 days, 10:10:10.10" (required),
    * "description": "string" (required)

    Также будет создана google таблица, в которую запишутся все полученные данные. Доступ к файлу будет аккаунта почты, указанного в .env.



### Стек: 
* FastAPI = 0.78.0
* SQLAlchemy = 1.4.36
* Alembic = 1.7.7
* aiogoogle = 4.2.0
* SQLite

## Автор: mitsushidu