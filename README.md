# 📋 Subscription Manager

Сервис для управления личными подписками с REST API.

## 🚀 Возможности

- ✅ Добавление, редактирование, удаление подписок
- ✅ Отслеживание дат платежей
- ✅ Поддержка разных валют и периодов оплаты
- ✅ Полностью контейнеризирован (Docker)

## 🛠 Стек технологий

- **Backend:** Django 4.2 + Django REST Framework
- **Database:** PostgreSQL 15
- **Containerization:** Docker & Docker Compose
- **Testing:** pytest
- **OS:** Windows / Linux / Mac

## 📦 Быстрый старт

### Требования

- Docker Desktop
- Git

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ТВОЙ_НИК/subscription-manager.git
cd subscription-manager
```

2. Создайте файл .env:
```
cp .env.example .env
```

3. Запустите проект:
```
docker-compose exec web pytest
```

4. Откройте браузер: http://127.0.0.1:8000/api/

## 📡 API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/subscriptions/` | Получить все подписки |
| POST | `/api/subscriptions/` | Создать подписку |
| GET | `/api/subscriptions/{id}/` | Получить подписку по ID |
| PUT | `/api/subscriptions/{id}/` | Обновить подписку |
| DELETE | `/api/subscriptions/{id}/` | Удалить подписку |

🔐 Безопасность

    Пароли базы данных хранятся в .env
    .env добавлен в .gitignore
    Не содержит секретов в репозитории

👨‍💻 Автор
[Oleg Markin] — Junior Python Developer

📄 Лицензия
MIT