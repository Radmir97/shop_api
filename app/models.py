from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    """
    Модель пользователя системы.
    
    Attributes:
        id (int): Уникальный идентификатор пользователя
        email (str): Email пользователя (используется как логин)
        hashed_password (str): Хешированный пароль пользователя
        is_active (bool): Статус активности пользователя
        created_at (datetime): Дата и время создания пользователя
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    """
    Модель товара в магазине.
    
    Attributes:
        id (int): Уникальный идентификатор товара
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        stock (int): Количество товара на складе
        created_at (datetime): Дата и время создания товара
        updated_at (datetime): Дата и время последнего обновления товара
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 