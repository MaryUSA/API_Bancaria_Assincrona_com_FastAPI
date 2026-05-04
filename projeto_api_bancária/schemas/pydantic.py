from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# --- Schemas de Autenticação ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- Schemas de Transação ---

# O que o usuário envia para criar uma transação
class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, description="O valor deve ser maior que zero")
    description: str = Field(..., min_length=3, max_length=100)
    target_account: str = Field(..., example="12345-6")

# O que a API retorna (herda de TransactionCreate + campos do banco)
class TransactionResponse(TransactionCreate):
    id: int
    created_at: datetime

    class Config:
        # Permite que o Pydantic leia dados que venham como objetos do SQLAlchemy (ORM)
        from_attributes = True

# --- Schemas de Usuário (Para o Cadastro/Login) ---
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

