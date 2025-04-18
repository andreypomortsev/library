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
│   ├── core
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
- **`README.ru.md`**: Markdown file containing project information in Russian.
- **`app/`**: Directory containing FastAPI application files.
  - **`Dockerfile`**: Docker configuration for the FastAPI application.
  - **`main.py`**: Main entry point for the FastAPI application.
  - **`requirements.txt`**: Python dependencies for the application.
  - **`routers/`**: Directory containing route handlers for different entities (books, customers, loans).
  - **`schemas/`**: Schemas for defining data models (book, customer, loan).
  - **`services/`**: Business logic services (book_service, customer_service, loan_service).
  - **`core/`**:Directory containing database-related files specific to the FastAPI application.
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
