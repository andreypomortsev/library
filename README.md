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
  <summary><h3>Endpoints</h3></summary>

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
      ...
    ]
    ```
  - *Описание*: Этот эндпоинт возвращает список всех авторов с возможностью пагинации. Параметры `skip` и `limit` позволяют пропустить определенное количество записей в начале списка и ограничить количество возвращаемых записей, соответственно.
</details>

## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

## Лицензия

Этот проект лицензируется по лицензии MIT - подробности см. в файле [LICENSE](./LICENSE).
