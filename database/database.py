from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных SQLite
DATABASE_URL = "sqlite:///./test.db"  # Для SQLite
# DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Для PostgreSQL
# DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"  # Для MySQL

# Создание движка базы данных
engine = create_engine(DATABASE_URL)

# Создание фабрики сессий для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базовой модели для декларативного определения моделей
Base = declarative_base()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db  # Возвращает сессию базы данных
    finally:
        db.close()  # Закрывает сессию после использования