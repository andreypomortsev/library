-- Создаем функцию для проверки статуса книги и добавления новой записи о выдаче
CREATE OR REPLACE FUNCTION create_book_loan(
    p_book_id INTEGER,
    p_user_id INTEGER,
    p_loan_date DATE,
    p_return_date DATE
) RETURNS VOID AS $$
DECLARE
    v_status BOOLEAN;
BEGIN
    -- Проверяем статус книги
    SELECT status INTO v_status FROM books WHERE bookId = p_book_id;

    -- Если книга не найдена, выбрасываем ошибку
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Не смогли найти книгу %', p_book_id;
    END IF;

    -- Если книга уже выдана, выбрасываем ошибку
    IF v_status = FALSE THEN
        RAISE EXCEPTION 'Книга с id сдана', p_book_id;
    END IF;

    -- Вставляем новую запись о выдаче книги
    INSERT INTO loans (book_id, user_id, loan_date, return_date)
    VALUES (p_book_id, p_user_id, p_loan_date, p_return_date);

    -- Обновляем статус книги на false (выдана)
    UPDATE books
    SET status = FALSE
    WHERE bookId = p_book_id;
END;
$$ LANGUAGE plpgsql;

-- Создаем функцию для обновления статуса книги
CREATE OR REPLACE FUNCTION update_book_status_after_loan(
    p_book_id INTEGER
) RETURNS VOID AS $$
BEGIN
    -- Обновляем статус книги на false (выдана)
    UPDATE books
    SET status = FALSE
    WHERE bookId = p_book_id;
    
    -- Проверяем, была ли затронута какая-либо строка
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Не смогли найти книгу %', p_book_id;
    END IF;
END;
$$ LANGUAGE plpgsql;
