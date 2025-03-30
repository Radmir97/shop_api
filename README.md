# Shop API

Простой API магазина с возможностью управления товарами и аутентификацией пользователей.

## Технологии

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT для аутентификации
- Docker

## Предварительные требования

- Python 3.8+
- PostgreSQL
- pip (менеджер пакетов Python)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Radmir97/shop_api
cd shop-api
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv\Scripts\activate  # для Windows
source venv/bin/activate     # для Linux/MacOS
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта:
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shop
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Примените миграции:
```bash
# Создание миграции
alembic revision --autogenerate -m "Initial migration"

# Применение миграции
alembic upgrade head
```

6. Запустите сервер:
```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/docs

## Запуск с помощью Docker

Если вы предпочитаете использовать Docker:

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Radmir97/shop_api
cd shop-api
```

2. Запустите приложение с помощью Docker Compose:
```bash
docker-compose up --build
```

При запуске Docker-контейнера автоматически:
- Создаются все необходимые таблицы в базе данных
- Применяются миграции
- Создаются тестовые данные
- Запускается приложение

Приложение будет доступно по адресу: http://127.0.0.1:8000/docs

## Тестовые данные

При первом запуске приложения автоматически создаются тестовые данные:

### Тестовый пользователь
- Email: test@example.com
- Пароль: test123

### Тестовые товары
1. Смартфон
   - Цена: 29999.99
   - В наличии: 10 шт.
   - Описание: Современный смартфон с хорошей камерой

2. Ноутбук
   - Цена: 59999.99
   - В наличии: 5 шт.
   - Описание: Мощный ноутбук для работы и игр

3. Наушники
   - Цена: 7999.99
   - В наличии: 15 шт.
   - Описание: Беспроводные наушники с шумоподавлением

## API Endpoints

### Аутентификация

- POST `/api/register` - Регистрация нового пользователя
- POST `/api/token` - Получение токена доступа

### Товары

- GET `/api/products` - Получить список всех товаров
- GET `/api/products/{product_id}` - Получить информацию о конкретном товаре
- POST `/api/products` - Создать новый товар (требуется аутентификация)
- PUT `/api/products/{product_id}` - Обновить товар (требуется аутентификация)
- DELETE `/api/products/{product_id}` - Удалить товар (требуется аутентификация)

## Примеры использования

### Регистрация пользователя

```bash
curl -X POST "http://127.0.0.1:8000/api/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123"}'
```

### Получение токена

```bash
curl -X POST "http://127.0.0.1:8000/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password123"
```

### Создание товара

```bash
curl -X POST "http://127.0.0.1:8000/api/products" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Product Name", "description": "Description", "price": 99.99, "stock": 10}'
``` 


## Ошибки
### 1. .idea/ не добавлен в .gitignore
IDE-шные файлы не должны попадать в репозиторий.

### 2. .env не добавлен в .gitignore
Файл .env может содержать чувствительные данные (пароли, секретные ключи), его нельзя коммитить.

### 3. README.md не содержит полного описания запуска проекта:

После git clone нужно:

- установить зависимости:
```
pip install -r requirements.txt
```
- создать и настроить .env

- применить миграции (команды написать)

- запустить сервер (команда)

### 4. Папка с миграциями отсутствует

Видимо, была создана, но не добавлена в git. Проверь alembic/ или migrations/.

### 5. Используется устаревший способ загрузки переменных через dotenv
Лучше использовать pydantic.BaseSettings 

### 6. Нельзя использовать импорты с двумя точками

Например:
```
from ..models import User  # ❌ так нельзя
```
Нужно использовать абсолютные импорты:
```
from app.models import User  # ✅ правильно
```

### 7. routers/ используется не по назначению

В routers должны быть только маршруты (эндпоинты), а логика работы с БД должна быть в crud/.

Пример:

routers/user.py — @router.get("/users/")

crud/user.py — get_user_by_id(db, id)