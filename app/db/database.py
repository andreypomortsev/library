from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://admin:password@db/library"

# Создание движка SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание класса SessionLocal для работы с сеансами базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Зависимая функция для обеспечения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
