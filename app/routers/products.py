from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from .auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Создает новый товар.
    
    Args:
        product (schemas.ProductCreate): Данные нового товара
        db (Session): Сессия базы данных
        current_user (models.User): Текущий аутентифицированный пользователь

    Returns:
        models.Product: Созданный товар
    """
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[schemas.Product])
def read_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Получает список товаров с пагинацией.
    
    Args:
        skip (int): Количество пропускаемых записей
        limit (int): Максимальное количество возвращаемых записей
        db (Session): Сессия базы данных

    Returns:
        List[models.Product]: Список товаров
    """
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    """
    Получает информацию о конкретном товаре.
    
    Args:
        product_id (int): Идентификатор товара
        db (Session): Сессия базы данных

    Returns:
        models.Product: Найденный товар

    Raises:
        HTTPException: Если товар не найден
    """
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Обновляет информацию о товаре.
    
    Args:
        product_id (int): Идентификатор товара
        product (schemas.ProductCreate): Новые данные товара
        db (Session): Сессия базы данных
        current_user (models.User): Текущий аутентифицированный пользователь

    Returns:
        models.Product: Обновленный товар

    Raises:
        HTTPException: Если товар не найден
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Удаляет товар.
    
    Args:
        product_id (int): Идентификатор товара
        db (Session): Сессия базы данных
        current_user (models.User): Текущий аутентифицированный пользователь

    Returns:
        dict: Сообщение об успешном удалении

    Raises:
        HTTPException: Если товар не найден
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"} 