from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Async Banking API")

# --- Mock de Segurança (Para o exemplo ser funcional) ---
SECRET_KEY = "sua_chave_secreta_super_segura"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Schemas ---
class TransactionCreate(BaseModel):
    amount: float
    description: str
    target_account: str

class TransactionResponse(TransactionCreate):
    id: int
    timestamp: datetime

# --- Autenticação ---
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Aqui você validaria no banco de dados
    if form_data.username != "admin":
        raise HTTPException(status_code=400, detail="Usuário incorreto")
    return {"access_token": form_data.username, "token_type": "bearer"}

# --- Funcionalidade 1: Cadastro de Transações (Assíncrono) ---
@app.post("/transactions/", response_model=TransactionResponse, status_code=201)
async def create_transaction(tx: TransactionCreate, token: str = Depends(oauth2_scheme)):
    # Simulação de salvamento assíncrono no banco
    return {**tx.dict(), "id": 1, "timestamp": datetime.now()}

# --- Funcionalidade 2: Exibição de Contrato ---
@app.get("/contract/")
async def get_contract(token: str = Depends(oauth2_scheme)):
    return {
        "title": "Termos de Uso Bancário",
        "content": "Ao utilizar esta API, você concorda com o processamento assíncrono de dados.",
        "version": "2024.1"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
