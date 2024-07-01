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


CREATE OR REPLACE FUNCTION return_book(
    p_book_id INTEGER,
    p_return_date DATE
) RETURNS VOID AS $$
DECLARE
    v_status BOOLEAN;
    v_loan_id INTEGER;
BEGIN
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

    -- Получаем id выдачи по id книги
    SELECT id INTO v_loan_id FROM loans WHERE book_id = p_book_id AND return_date IS NULL;

    -- Если выдача не найдена, выбрасываем ошибку
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Не смогли найти выдачу для книги с id %', p_book_id;
    END IF;

    -- Обновляем запись о выдаче книги
    UPDATE loans
    SET return_date = p_return_date
    WHERE id = v_loan_id;

    -- Обновляем статус книги на true (доступна)
    UPDATE books
    SET status = TRUE
    WHERE id = p_book_id;
END;
$$ LANGUAGE plpgsql;
