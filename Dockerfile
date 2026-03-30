# Базовый образ с Python 3.14
FROM python:3.14-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости для PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Порт, который будет слушать Django
EXPOSE 8000

# Команда запуска (используем gunicorn для продакшена, но для разработки оставим runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]