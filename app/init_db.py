from sqlalchemy.orm import Session
from . import models, utils

def init_db(db: Session) -> None:
    # Создаем тестового пользователя
    user = db.query(models.User).filter(models.User.email == "test@example.com").first()
    if not user:
        hashed_password = utils.get_password_hash("test123")
        user = models.User(
            email="test@example.com",
            hashed_password=hashed_password,
            is_active=True
        )
        db.add(user)
        db.commit()

    # Создаем тестовые товары
    products = [
        {
            "name": "Смартфон",
            "description": "Современный смартфон с хорошей камерой",
            "price": 29999.99,
            "stock": 10
        },
        {
            "name": "Ноутбук",
            "description": "Мощный ноутбук для работы и игр",
            "price": 59999.99,
            "stock": 5
        },
        {
            "name": "Наушники",
            "description": "Беспроводные наушники с шумоподавлением",
            "price": 7999.99,
            "stock": 15
        }
    ]

    for product_data in products:
        product = db.query(models.Product).filter(models.Product.name == product_data["name"]).first()
        if not product:
            product = models.Product(**product_data)
            db.add(product)
    
    db.commit() 