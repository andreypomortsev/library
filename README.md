![Static Badge](https://img.shields.io/badge/Python-3.12%2B-blue)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)
# Library Management System

## The Project Tree

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
│   │   ├── book.py
│   │   ├── customer.py
│   │   └── loan.py
│   └── services
│       ├── book_service.py
│       ├── customer_service.py
│       └── loan_service.py
├── db
│   ├── Dockerfile
│   ├── init.sql
│   └── procedures.sql
└── docker-compose.yml
```

### Structure Explanation:

- **`LICENSE`**: File containing the MIT License details.
- **`README.md`**: Markdown file containing project information.
- **`app/`**: Directory containing FastAPI application files.
  - **`Dockerfile`**: Docker configuration for the FastAPI application.
  - **`main.py`**: Main entry point for the FastAPI application.
  - **`requirements.txt`**: Python dependencies for the application.
  - **`routers/`**: Directory containing route handlers for different entities (books, customers, loans).
  - **`schemas/`**: Schemas for defining data models (book, customer, loan).
  - **`services/`**: Business logic services (book_service, customer_service, loan_service).
  - **`db/`**:Directory containing database-related files specific to the FastAPI application.
    - **`database.py`**: Database connection setup.
    - **`models.py`**: SQLAlchemy models for database tables.
- **`db/`**: Directory containing database-related files.
  - **`Dockerfile`**: Docker configuration for the database.
  - **`init.sql`**: SQL script for initializing the database schema.
  - **`procedures.sql`**: SQL script for stored procedures.
- **`docker-compose.yml`**: YAML file defining Docker services for the application and database.


### Prerequisites

- Docker
- Docker Compose

### Run

1. Clone the repo:
   ```sh
   git clone https://github.com/andreypomortsev/library.git
   cd library
   ```

2. Running the services:
   ```sh
   docker compose up --build
   ```

3. The FastAPI is available at `http://localhost:8000`.
4. The API documentation is available at `http://localhost:8000/docs`.

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

   ### Customers /Пользователи/ 
- **POST /users**: Создать нового пользователя
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

- **POST /users**: Создать нового автора
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

- **PUT /users/{user_id}**: Изменить данные пользователя по ID
  - *Параметры пути*: `user_id` - ID пользователя для изменения
  - *Тело запроса*: JSON с обновленными данными пользователя (необязательные поля)
    ```json
    {
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995,
      "is_author": false
    }
    ```
  - *Ответ*: JSON с обновленными данными пользователя
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

- **GET /users/{user_id}**: Получить пользователя по ID
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

- **GET /users**: Получить список всех пользователей с пагинацией
  - *Параметры запроса*:
    - `skip` (optional, default=0): Количество записей, которые следует пропустить в начале списка.
    - `limit` (optional, default=50): Максимальное количество записей, которые следует вернуть (ограничение на количество записей).
  - *Ответ*: JSON со списком пользователей (**не авторов**) согласно указанным параметрам пагинации.
    ```json
    [
      {
        "id": 1,
        "name": "Новое Имя",
        "last_name": "Новая Фамилия",
        "middle_name": "Новое Отчество",
        "birth_year": 1995,
        "is_author": false
      }
    ]
    ```
- **GET /users**: Получить список всех авторов с пагинацией
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
### Books /Книги/

- **POST /books**: Создание новой книги
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

- **PUT /books/{book_id}**: Изменить данные книги по ID
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
- **GET /books**: Получить все книги с пагинацией
  - *Параметры запроса*:
    - `skip` (optional, default=0): Количество записей, которые следует пропустить в начале списка.
    - `limit` (optional, default=10): Максимальное количество записей, которые следует вернуть (ограничение на количество записей).
  - *Ответ*: JSON со списком авторов согласно указанным параметрам пагинации.
    ```json
    [
      {
        "id": 1,
        "title": "Новое Название",
        "author_id": "1",
        "genre": "Новый жанр",
        "year": 1986,
        "status": false
      }
    ]
    ```
### Loans /Аренда книг/
- **POST /loans**: Создание сдачи книги в аренду
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

- **PUT /loans/{book_id}**: Вернуть книгу по ID
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

- **GET /loans**: Получить список всех аренд с пагинацией
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

## Author

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

## License

This project is licensed under the MIT License - see the file for details [LICENSE](./LICENSE).
