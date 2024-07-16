from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:password@db/library"

# Create the SQLAlchemy engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Dependency to get a database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
