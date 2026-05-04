from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# URL para PostgreSQL (exemplo). Use 'sqlite+aiosqlite:///./test.db' para testes locais rápidos.
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# Dependência para o FastAPI
async def get_db():
    async with async_session() as session:
        yield session
