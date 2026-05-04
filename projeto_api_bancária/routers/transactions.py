from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from core.database import get_db
from core.auth import get_current_user
from models.tables import Transaction
from schemas.pydantic import TransactionCreate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transações"]
)

@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(
    tx_data: TransactionCreate, 
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Cria uma nova transação financeira de forma assíncrona.
    Requer autenticação JWT.
    """
    # Criamos a instância do modelo SQLAlchemy
    new_transaction = Transaction(
        amount=tx_data.amount,
        description=tx_data.description,
        target_account=tx_data.target_account
    )
    
    db.add(new_transaction)
    
    try:
        await db.commit()       # Salva no banco de forma assíncrona
        await db.refresh(new_transaction) # Atualiza o objeto com o ID gerado
        return new_transaction
    except Exception as e:
        await db.rollback()     # Desfaz em caso de erro
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao processar transação."
        )

@router.get("/", response_model=List[TransactionResponse])
async def list_transactions(
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Lista todas as transações cadastradas.
    """
    result = await db.execute(select(Transaction))
    transactions = result.scalars().all()
    return transactions

