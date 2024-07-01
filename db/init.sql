-- Создаем таблицу пользователей, которые могут быть авторами
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    birth_year INTEGER NOT NULL,
    is_author BOOLEAN NOT NULL DEFAULT FALSE
);

-- Создаем таблицу books
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER REFERENCES customers(id),
    genre VARCHAR(255) NOT NULL,
    year INTEGER NOT NULL,
    status BOOLEAN NOT NULL DEFAULT TRUE
);

-- Создаем таблицу loans
CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id) NOT NULL,
    user_id INTEGER REFERENCES customers(id) NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE DEFAULT NULL
);

-- Добавляем хранимые процедуры
\i /docker-entrypoint-initdb.d/procedures.sql