from fastapi import APIRouter, Depends
from core.auth import get_current_user

router = APIRouter(
    prefix="/contract",
    tags=["Contrato"]
)

@router.get("/")
async def show_contract(current_user: str = Depends(get_current_user)):
    """
    Exibe os termos do contrato bancário. 
    Acesso restrito a usuários autenticados via JWT.
    """
    return {
        "user_authenticated": current_user,
        "document_type": "Contrato de Abertura de Conta Corrente",
        "version": "2024.2.1",
        "clauses": [
            {
                "id": 1,
                "title": "Do Objeto",
                "content": "Este contrato rege as condições de uso da API bancária assíncrona."
            },
            {
                "id": 2,
                "title": "Da Segurança",
                "content": "O usuário é responsável por manter a confidencialidade de suas credenciais JWT."
            },
            {
                "id": 3,
                "title": "Do Processamento",
                "content": "As transações são processadas de forma assíncrona para garantir alta disponibilidade."
            }
        ],
        "footer": "© 2024 Async Bank - Todos os direitos reservados."
    }
