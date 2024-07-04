# Управление выдачей/взврата книг в библиотеке

## Структура проекта

```
library/
├── LICENSE
├── README.md
├── app
│   ├── Dockerfile
│   ├── db
│   │   ├── database.py
│   │   └── models.py
│   ├── main.py
│   ├── requirements.txt
│   ├── routers
│   │   ├── books.py
│   │   ├── customers.py
│   │   └── loans.py
│   └── schemas
│       ├── book.py
│       ├── customer.py
│       └── loan.py
├── db
│   ├── Dockerfile
│   ├── init.sql
│   └── procedures.sql
└── docker-compose.yml
```

### Предварительные требования

- Docker
- Docker Compose

### Запуск приложения

1. Клонируем репозиторий:
   ```sh
   git clone https://github.com/andreypomortsev/library.git
   cd library
   ```

2. Создание и запуск сервисов:
   ```sh
   docker-compose up --build
   ```

3. The FastAPI сервис будет доступен по адресу `http://localhost:8000`, проверить документацию можно тут `http://localhost:8000/docs`.

<details>
  <summary><h2>Database Schema</h2></summary>

   #### Here is a representation of the database schema for the project:

### Table: `customers`

| Column       | Type          | Constraints                    |
|--------------|---------------|--------------------------------|
| id           | SERIAL        | PRIMARY KEY                    |
| name         | VARCHAR(100)  | NOT NULL                       |
| last_name    | VARCHAR(100)  | NOT NULL                       |
| middle_name  | VARCHAR(100)  |                                |
| birth_year   | INTEGER       | NOT NULL                       |
| is_author    | BOOLEAN       | NOT NULL, DEFAULT FALSE        |

### Table: `books`

| Column    | Type         | Constraints                         |
|-----------|--------------|-------------------------------------|
| id        | SERIAL       | PRIMARY KEY                         |
| title     | VARCHAR(255) | NOT NULL                            |
| author_id | INTEGER      | REFERENCES customers(id)            |
| genre     | VARCHAR(255) | NOT NULL                            |
| year      | INTEGER      | NOT NULL                            |
| status    | BOOLEAN      | NOT NULL, DEFAULT TRUE              |

### Table: `loans`

| Column      | Type    | Constraints                          |
|-------------|---------|--------------------------------------|
| id          | SERIAL  | PRIMARY KEY                          |
| book_id     | INTEGER | REFERENCES books(id), NOT NULL       |
| user_id     | INTEGER | REFERENCES customers(id), NOT NULL   |
| loan_date   | DATE    | NOT NULL, DEFAULT CURRENT_DATE       |
| return_date | DATE    | DEFAULT NULL                         |
</details>

<details>
  <summary><h2>Endpoints</h2></summary>

   ### Пользователи
- **POST /user/create**: Создать нового пользователя
  - *Тело запроса*:
     ```json
    {
      "name": "Имя",
      "last_name": "Фамилия",
      "middle_name": "Отчество",
      "birth_year": 1990,
    }
    ```
  - *Ответ*: JSON с созданным пользователем
    ```json
    {
      "id": 1,
      "name": "Имя",
      "last_name": "Фамилия",
      "middle_name": "Отчество",
      "birth_year": 1990,
      "is_author": false
    }
    ```

- **POST /user/create**: Создать нового автора
  - *Тело запроса*:
     ```json
       {
         "name": "Имя Автора",
         "last_name": "Фамилия Автора",
         "middle_name": "Отчество Автора",
         "birth_year": 1990,
         "is_author": true
       }
    ```
  - *Ответ*: JSON с созданным пользователем
    ```json
    {
      "id": 2,
      "name": "Имя Автора",
      "last_name": "Фамилия Автора",
      "middle_name": "Отчество Автора",
      "birth_year": 1990,
      "is_author": true
    }
    ```

- **PUT /user/{user_id}/edit**: Изменить данные автора по ID
  - *Параметры пути*: `user_id` - ID автора для изменения
  - *Тело запроса*: JSON с обновленными данными автора (необязательные поля)
    ```json
    {
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995,
      "is_author": false
    }
    ```
  - *Ответ*: JSON с обновленными данными автора
    ```json
    {
      "id": 1,
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995,
      "is_author": false
    }
    ```

- **GET /user/{user_id}**: Получить пользователя по ID
  - *Параметры пути*: `user_id` - ID пользователя для получения данных
  - *Ответ*: JSON с данными пользователя по указанному ID
    ```json
    {
      "id": 1,
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995,
      "is_author": false
    }
    ```

- **GET /users/**: Получить список всех авторов с пагинацией
  - *Параметры запроса*:
    - `skip` (optional, default=0): Количество записей, которые следует пропустить в начале списка.
    - `limit` (optional, default=50): Максимальное количество записей, которые следует вернуть (ограничение на количество записей).
  - *Ответ*: JSON со списком авторов согласно указанным параметрам пагинации.
    ```json
    [
      {
        "id": 2,
        "name": "Имя Автора",
        "last_name": "Фамилия Автора",
        "middle_name": "Отчество Автора",
        "birth_year": 1990,
        "is_author": true
      }
    ]
    ```
  - *Описание*: Этот эндпоинт возвращает список всех авторов с возможностью пагинации. Параметры `skip` и `limit` позволяют пропустить определенное количество записей в начале списка и ограничить количество возвращаемых записей, соответственно.
### Книги

- **POST /books/create**: Создание новой книги
  - *Тело запроса*:
     ```json
    {
      "title": "It",
      "author_id": "1",
      "genre": "Horror",
      "year": 1985,
      "status": true
    }
    ```
  - *Ответ*: JSON с созданной книгой
    ```json
    {
      "id": 1,
      "title": "It",
      "author_id": "1",
      "genre": "Horror",
      "year": 1985,
      "status": true
    }
    ```

- **PUT /books/{book_id}/edit**: Изменить данные книги по ID
  - *Параметры пути*: `book_id` - ID книги для изменения
  - *Тело запроса*: JSON с обновленными данными книги (необязательные поля)
    ```json
    {
      "title": "Новое Название",
      "author_id": "1",
      "genre": "Новый жанр",
      "year": 1986,
      "status": false
    }
    ```
  - *Ответ*: JSON с обновленными данными книги
    ```json
    {
      "id": 1,
      "title": "Новое Название",
      "author_id": "1",
      "genre": "Новый жанр",
      "year": 1986,
      "status": false
    }
    ```

- **GET /books/{book_id}**: Получить книгу по ID
  - *Параметры пути*: `book_id` - ID книги для получения данных
  - *Ответ*: JSON с данными книги по указанному ID
    ```json
    {
      "id": 1,
      "title": "Новое Название",
      "author_id": "1",
      "genre": "Новый жанр",
      "year": 1986,
      "status": false
    }
    ```

### Аренда книг
- **POST /loans/create**: Создание сдачи книги в аренду
  - *Тело запроса*:
     ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01"
    }
    ```
  - *Ответ*: JSON с созданным арендой
    ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01",
      "return_date": null
    }
    ```

- **PUT /loans/{book_id}/edit**: Вернуть книгу по ID
  - *Параметры пути*: `book_id` - ID книги для изменения
  - *Тело запроса*: JSON с ID книги и датой возврата (необязательное поле)
    ```json
    {
      "book_id": 1,
      "return_date": "2024-06-13"
    }
    ```
  - *Ответ*: JSON с обновленными данными аренды
    ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01",
      "return_date": "2024-06-13"
    }
    ```

- **GET /loans/**: Получить список всех аренд с пагинацией
  - *Параметры запроса*:
    - `skip` (optional, default=0): Количество записей, которые следует пропустить в начале списка.
    - `limit` (optional, default=50): Максимальное количество записей, которые следует вернуть (ограничение на количество записей).
  - *Ответ*: JSON с данными книги по указанному ID
    ```json
    [
       {
         "id": 1,
         "book_id": 1,
         "user_id": 1,
         "loan_date": "2024-06-01",
         "return_date": "2024-06-13"
       }
    ]
    ```
</details>

## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

## Лицензия

Этот проект лицензируется по лицензии MIT - подробности см. в файле [LICENSE](./LICENSE).
