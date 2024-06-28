FROM python:3.11-slim

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /app

# Создаем нового пользователя
RUN useradd -m non_root
# Гарантируем права доступа
RUN chown -R non_root:non_root /app
# Меняем пользователя
USER non_root

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]