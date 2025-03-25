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

- Docker
- Docker Compose

## Установка и запуск с помощью Docker

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd shop-api
```

2. Запустите приложение с помощью Docker Compose:
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000/docs

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

### Регистрация пользователя (Происходит автоматически)

```bash
curl -X POST "http://localhost:8000/api/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123"}'
```

### Получение токена

```bash
curl -X POST "http://localhost:8000/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password123"
```

### Создание товара

```bash
curl -X POST "http://localhost:8000/api/products" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Product Name", "description": "Description", "price": 99.99, "stock": 10}'
``` 