-- Создаем функцию для проверки статуса книги и добавления новой записи о выдаче
CREATE OR REPLACE FUNCTION create_book_loan(
    p_book_id INTEGER,
    p_user_id INTEGER,
    p_loan_date DATE
) RETURNS VOID AS $$
DECLARE
    v_status BOOLEAN;
BEGIN
    -- Проверяем статус книги
    SELECT status INTO v_status FROM books WHERE id = p_book_id;

    -- Если книга не найдена, выбрасываем ошибку
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Не смогли найти книгу %', p_book_id;
    END IF;

    -- Если книга уже выдана, выбрасываем ошибку
    IF v_status = FALSE THEN
        RAISE EXCEPTION 'Книга с id % уже выдана', p_book_id;
    END IF;

    -- Вставляем новую запись о выдаче книги
    INSERT INTO loans (book_id, user_id, loan_date)
    VALUES (p_book_id, p_user_id, p_loan_date);

    -- Обновляем статус книги на false (выдана)
    UPDATE books
    SET status = FALSE
    WHERE id = p_book_id;
END;
$$ LANGUAGE plpgsql;


-- Создаем функцию для проверки возврата книги и добавления даты возврата
CREATE OR REPLACE FUNCTION return_book(
    p_loan_id INTEGER
) RETURNS VOID AS $$
DECLARE
    v_status BOOLEAN;
    p_book_id INTEGER;
BEGIN
    -- Получаем id книги
    SELECT book_id INTO p_book_id FROM loans WHERE id = p_loan_id;

    -- Проверяем статус книги
    SELECT status INTO v_status FROM books WHERE id = p_book_id;

    -- Если книга не найдена, выбрасываем ошибку
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Не смогли найти книгу с id %', p_book_id;
    END IF;

    -- Если книга уже доступна, выбрасываем ошибку
    IF v_status = TRUE THEN
        RAISE EXCEPTION 'Книга с id % уже доступна', p_book_id;
    END IF;

    -- Обновляем запись о выдаче книги
    UPDATE loans
    SET return_date = CURRENT_DATE
    WHERE id = p_loan_id;

    -- Обновляем статус книги на true (доступна)
    UPDATE books
    SET status = TRUE
    WHERE id = p_book_id;
END;
$$ LANGUAGE plpgsql;

-- Функция которая получает автора по имени и фамилии
CREATE OR REPLACE FUNCTION get_author_id_by_name_last_name(
    author_name VARCHAR(255),
    author_last_name VARCHAR(255),
    author_birth_year INTEGER
) RETURNS INTEGER AS $$
DECLARE
    author_id INTEGER;
BEGIN
    SELECT id INTO author_id
    FROM authors
    WHERE name = author_name AND last_name = author_last_name AND birth_year = author_birth_year;

    RETURN author_id;
END;
$$ LANGUAGE plpgsql;
