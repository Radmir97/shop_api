from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, products
from app.database import engine, Base, SessionLocal
from app.init_db import init_db

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Инициализируем базу данных с тестовыми данными
db = SessionLocal()
init_db(db)
db.close()

app = FastAPI(title="Shop API")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])

@app.get("/")
async def root():
    return {"message": "Welcome to Shop API"} 