![Static Badge](https://img.shields.io/badge/Python-3.12%2B-blue)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)
# Система управления библиотекой

## Структура проекта

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
│   ├── schemas
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
├── docker-compose.yml
└── docs
    ├── api.md
    └── api.ru.md
```

### Описание структуры:

- **`LICENSE`**: Лицензия MIT для проекта.  
- **`README.md`**: Основная документация проекта на английском языке.  
- **`README.ru.md`**: Документация проекта на русском языке.  
- **`app/`**: Исходный код приложения на FastAPI.  
  - **`Dockerfile`**: Конфигурация Docker для приложения FastAPI.  
  - **`main.py`**: Точка входа в приложение, включает регистрацию маршрутов.  
  - **`requirements.txt`**: Список зависимостей Python.  
  - **`core/`**: Основные утилиты и конфигурация.  
    - **`database.py`**: Настройка подключения к базе данных и управление сессиями.  
  - **`models/`**: ORM-модели SQLAlchemy, соответствующие таблицам базы данных.  
    - **`book.py`**, **`customer.py`**, **`loan.py`**: Модели для соответствующих сущностей.  
  - **`routers/`**: Определения маршрутов (API endpoints).  
    - **`books.py`**, **`customers.py`**, **`loans.py`**: Роутеры для операций с соответствующими ресурсами.  
  - **`schemas/`**: Pydantic-схемы для валидации запросов и сериализации ответов.  
    - Повторяют структуру `models/` для согласованности.  
  - **`services/`**: Слой бизнес-логики, отделяющий её от маршрутов.  
    - Сервисные функции для работы с книгами, пользователями и займами.  
- **`db/`**: Инициализация и конфигурация базы данных.  
  - **`Dockerfile`**: Настройка PostgreSQL в контейнере.  
  - **`init.sql`**: SQL-скрипт для создания таблиц и начального наполнения.  
  - **`procedures.sql`**: Содержит хранимые процедуры, используемые в приложении.  
- **`docker-compose.yml`**: Оркестрация сервисов FastAPI и PostgreSQL.  
- **`docs/`**: Документация API на английском и русском языках.  

### Предварительные требования

- Docker  
- Docker Compose

### Запуск

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/andreypomortsev/library.git
   cd library
   ```

2. Запустите сервисы:
   ```sh
   docker compose up --build
   ```

3. FastAPI будет доступен по адресу `http://localhost:8000`.  
4. Документация API доступна по адресу `http://localhost:8000/docs`.

## Схема базы данных

### Ниже представлена схема базы данных проекта:

#### Таблица: `customers`

| Колонка      | Тип           | Ограничения                    |
|--------------|----------------|--------------------------------|
| id           | SERIAL         | PRIMARY KEY                    |
| name         | VARCHAR(100)   | NOT NULL                       |
| last_name    | VARCHAR(100)   | NOT NULL                       |
| middle_name  | VARCHAR(100)   |                                |
| birth_year   | INTEGER        | NOT NULL                       |
| is_author    | BOOLEAN        | NOT NULL, DEFAULT FALSE        |

#### Таблица: `books`

| Колонка   | Тип          | Ограничения                          |
|-----------|---------------|--------------------------------------|
| id        | SERIAL        | PRIMARY KEY                          |
| title     | VARCHAR(255)  | NOT NULL                             |
| author_id | INTEGER       | REFERENCES customers(id)             |
| genre     | VARCHAR(255)  | NOT NULL                             |
| year      | INTEGER       | NOT NULL                             |
| status    | BOOLEAN       | NOT NULL, DEFAULT TRUE               |

#### Таблица: `loans`

| Колонка     | Тип     | Ограничения                           |
|-------------|----------|----------------------------------------|
| id          | SERIAL   | PRIMARY KEY                            |
| book_id     | INTEGER  | REFERENCES books(id), NOT NULL         |
| user_id     | INTEGER  | REFERENCES customers(id), NOT NULL     |
| loan_date   | DATE     | NOT NULL, DEFAULT CURRENT_DATE         |
| return_date | DATE     | DEFAULT NULL                           |

## 📚 Документация API

Подробный список доступных эндпоинтов:  
➡️ [Смотреть все эндпоинты](docs/api.ru.md)

## Вклад в проект

Приветствуются любые улучшения! Сделайте форк репозитория и отправьте Pull Request.

## Автор

- [Андрей Поморцев](https://www.linkedin.com/in/andreypomortsev/)

## Лицензия

Этот проект лицензирован под лицензией MIT – подробности смотрите в файле [LICENSE](./LICENSE).