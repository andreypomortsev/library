# Управление выдачей книг в библиотеке

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
│   │   ├── authors.py
│   │   └── books.py
│   └── schemas
│       ├── author.py
│       └── book.py
├── db
│   ├── Dockerfile
│   ├── init.sql
│   └── procedures.sql
└── docker-compose.yml
```

## Начинаем

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

Конечно, вот как будет отформатированный блок для README файла на GitHub:

Вот отформатированный блок для README файла на GitHub, соответствующий вашей схеме данных:

## Endpoints

- **POST /authors/create**: Создать нового автора
  - *Тело запроса*: `{"name": "Имя Автора", "last_name": "Фамилия Автора", "middle_name": "Отчество Автора", "birth_year": 1990}`
  - *Ответ*: JSON с созданным автором
    ```json
    {
      "id": 1,
      "name": "Имя Автора",
      "last_name": "Фамилия Автора",
      "middle_name": "Отчество Автора",
      "birth_year": 1990
    }
    ```

- **PUT /authors/{author_id}/edit**: Изменить данные автора по ID
  - *Параметры пути*: `author_id` - ID автора для изменения
  - *Тело запроса*: JSON с обновленными данными автора (необязательные поля)
    ```json
    {
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995
    }
    ```
  - *Ответ*: JSON с обновленными данными автора
    ```json
    {
      "id": 1,
      "name": "Новое Имя",
      "last_name": "Новая Фамилия",
      "middle_name": "Новое Отчество",
      "birth_year": 1995
    }
    ```

- **GET /authors/{author_id}**: Получить автора по ID
  - *Параметры пути*: `author_id` - ID автора для получения данных
  - *Ответ*: JSON с данными автора по указанному ID
    ```json
    {
      "id": 1,
      "name": "Имя Автора",
      "last_name": "Фамилия Автора",
      "middle_name": "Отчество Автора",
      "birth_year": 1990
    }
  Certainly! Here's a description of the endpoint `GET /authors/`:

- **GET /authors/**: Получить список всех авторов с пагинацией
  - *Параметры запроса*:
    - `skip` (optional, default=0): Количество записей, которые следует пропустить в начале списка.
    - `limit` (optional, default=50): Максимальное количество записей, которые следует вернуть (ограничение на количество записей).
  - *Ответ*: JSON со списком авторов согласно указанным параметрам пагинации.
    ```json
    [
      {
        "id": 1,
        "name": "Имя Автора",
        "last_name": "Фамилия Автора",
        "middle_name": "Отчество Автора",
        "birth_year": 1990
      },
      {
        "id": 2,
        "name": "Имя Автора 2",
        "last_name": "Фамилия Автора 2",
        "middle_name": null,
        "birth_year": 1985
      },
      ...
    ]
    ```
  - *Описание*: Этот эндпоинт возвращает список всех авторов с возможностью пагинации. Параметры `skip` и `limit` позволяют пропустить определенное количество записей в начале списка и ограничить количество возвращаемых записей, соответственно.


## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

## Лицензия

Этот проект лицензируется по лицензии MIT - подробности см. в файле [LICENSE](./LICENSE).
