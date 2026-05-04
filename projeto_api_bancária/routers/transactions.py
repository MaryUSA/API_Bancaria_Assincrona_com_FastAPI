from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from models.tables import Transaction
from schemas.pydantic import TransactionCreate

router = APIRouter()

@router.post("/transactions/")
async def create_tx(data: TransactionCreate, db: AsyncSession = Depends(get_db)):
    new_tx = Transaction(**data.dict())
    db.add(new_tx)
    await db.commit()  # Operação assíncrona
    await db.refresh(new_tx)
    return new_tx

