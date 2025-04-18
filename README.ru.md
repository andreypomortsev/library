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
│   │   ├── database.py
│   │   └── models.py
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

### Описание структуры:

- **`LICENSE`**: Файл с информацией о лицензии MIT.
- **`README.md`**: Файл с описанием проекта на Английском.
- **`README.ru.md`**: Файл с описанием проекта.
- **`app/`**: Каталог с файлами FastAPI-приложения.
  - **`Dockerfile`**: Конфигурация Docker для FastAPI.
  - **`main.py`**: Точка входа в приложение.
  - **`requirements.txt`**: Список зависимостей Python.
  - **`routers/`**: Обработчики маршрутов для сущностей (книги, пользователи, займы).
  - **`schemas/`**: Схемы Pydantic для моделей данных (книга, пользователь, заём).
  - **`services/`**: Бизнес-логика (book_service, customer_service, loan_service).
  - **`core/`**: Каталог с настройкой базы данных.
    - **`database.py`**: Настройка подключения к базе данных.
    - **`models.py`**: SQLAlchemy-модели таблиц базы данных.
- **`db/`**: Файлы, связанные с базой данных.
  - **`Dockerfile`**: Конфигурация Docker для БД.
  - **`init.sql`**: Скрипт инициализации схемы базы данных.
  - **`procedures.sql`**: Скрипт со встроенными процедурами.
- **`docker-compose.yml`**: Файл конфигурации Docker Compose для запуска сервисов.

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