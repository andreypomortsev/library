from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


SQLALCHEMY_DATABASE_URL = "postgresql://admin:password@db/library"

# Создание движка SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание класса SessionLocal для работы с сеансами базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_author_id_by_name_last_name(
    db: Session, author_name: str, author_last_name: str, author_birth_year: int
) -> int:
    query = text("""
        SELECT get_author_id_by_name_last_name(:author_name, :author_last_name, :author_birth_year)
    """)
    result = db.execute(
        query,
        {
            "author_name": author_name,
            "author_last_name": author_last_name,
            "author_birth_year": author_birth_year,
        },
    )
    author_id = result.scalar()  # Предполагаем что вернется одно значение
    return author_id if author_id else None


# Зависимая функция для обеспечения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
