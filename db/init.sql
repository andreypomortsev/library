-- Создаем таблицу authors
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    birth_year INTEGER NOT NULL
);

-- Создаем таблицу books
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER REFERENCES authors(id),
    genre VARCHAR(255) NOT NULL,
    year INTEGER NOT NULL,
    status BOOLEAN NOT NULL DEFAULT TRUE
);

-- Создаем таблицу users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    birth_year INTEGER NOT NULL
);

-- Создаем таблицу loans
CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id) NOT NULL,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE DEFAULT NULL
);
