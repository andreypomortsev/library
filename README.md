![Static Badge](https://img.shields.io/badge/Python-3.12%2B-blue)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)
# Library Management System

## The Project Tree

```
library/
├── LICENSE
├── README.md
├── README.ru.md
├── app
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── core
│   │   └── database.py
│   ├── models
│   │   ├── book.py
│   │   ├── customer.py
│   │   └── loan.py
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
└── docs
    ├── api.md
    └── api.ru.md
```

### 📚 Structure Explanation

- **`LICENSE`**: MIT License for the project.
- **`README.md`**: Main project documentation in English.
- **`README.ru.md`**: Project documentation in Russian.
- **`app/`**: FastAPI application source code.
  - **`Dockerfile`**: Docker setup for the FastAPI app.
  - **`main.py`**: Application entry point, includes router registration.
  - **`requirements.txt`**: Python dependencies list.
  - **`core/`**: Core utilities and configuration.
    - **`database.py`**: Database engine and session management.
  - **`models/`**: SQLAlchemy ORM models that map to database tables.
    - **`book.py`**, **`customer.py`**, **`loan.py`**: Models for respective entities.
  - **`routers/`**: Route definitions (API endpoints).
    - **`books.py`**, **`customers.py`**, **`loans.py`**: Routers for resource-specific operations.
  - **`schemas/`**: Pydantic schemas for request validation and response serialization.
    - Mirrors the structure of `models/` for consistency.
  - **`services/`**: Business logic layer, keeping routes clean and focused.
    - Service functions for books, customers, and loans.
- **`db/`**: Database initialization and configuration.
  - **`Dockerfile`**: PostgreSQL setup inside a container.
  - **`init.sql`**: SQL script to initialize tables and seed data.
  - **`procedures.sql`**: Contains stored procedures used by the app.
- **`docker-compose.yml`**: Orchestration of the FastAPI and PostgreSQL services.
- **`docs/`**: API documentation in both English and Russian.

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

## Database Schema

### Here is a representation of the database schema for the project:

#### Table: `customers`

| Column       | Type          | Constraints                    |
|--------------|---------------|--------------------------------|
| id           | SERIAL        | PRIMARY KEY                    |
| name         | VARCHAR(100)  | NOT NULL                       |
| last_name    | VARCHAR(100)  | NOT NULL                       |
| middle_name  | VARCHAR(100)  |                                |
| birth_year   | INTEGER       | NOT NULL                       |
| is_author    | BOOLEAN       | NOT NULL, DEFAULT FALSE        |

#### Table: `books`

| Column    | Type         | Constraints                         |
|-----------|--------------|-------------------------------------|
| id        | SERIAL       | PRIMARY KEY                         |
| title     | VARCHAR(255) | NOT NULL                            |
| author_id | INTEGER      | REFERENCES customers(id)            |
| genre     | VARCHAR(255) | NOT NULL                            |
| year      | INTEGER      | NOT NULL                            |
| status    | BOOLEAN      | NOT NULL, DEFAULT TRUE              |

#### Table: `loans`

| Column      | Type    | Constraints                          |
|-------------|---------|--------------------------------------|
| id          | SERIAL  | PRIMARY KEY                          |
| book_id     | INTEGER | REFERENCES books(id), NOT NULL       |
| user_id     | INTEGER | REFERENCES customers(id), NOT NULL   |
| loan_date   | DATE    | NOT NULL, DEFAULT CURRENT_DATE       |
| return_date | DATE    | DEFAULT NULL                         |

## API Documentation

Detailed list of available endpoints:  
➡️ [See full API list](docs/api.md)

## Contributing

Contributions are welcome! Please fork the repo and create a pull request.

## Author

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

## License

This project is licensed under the MIT License - see the file for details [LICENSE](./LICENSE).
