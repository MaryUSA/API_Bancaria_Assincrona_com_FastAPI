# API_Banc-ria_Ass-ncrona_com_FastAPI
Desafio desenvolvido no curso da Luizalabs - Back-end com Python - 2º Edição.
Uma API bancária robusta e assíncrona desenvolvida com **FastAPI**, focada em alta performance e segurança. Este projeto demonstra a implementação de transações financeiras, autenticação JWT e integração com banco de dados utilizando SQLAlchemy 2.0.

## 🚀 Tecnologias Utilizadas

*   **Python 3.10+**
*   **FastAPI**: Framework web moderno e rápido.
*   **SQLAlchemy 2.0**: ORM para interação com banco de dados (mapeamento assíncrono).
*   **Asyncpg**: Driver assíncrono para PostgreSQL.
*   **Pydantic V2**: Validação de dados e schemas.
*   **JWT (JSON Web Tokens)**: Segurança e autenticação de usuários.
*   **Uvicorn**: Servidor ASGI de alta performance.

## 🛠️ Funcionalidades

- [x] **Autenticação**: Sistema de login com geração de token JWT.
- [x] **Transações**: Cadastro assíncrono de movimentações financeiras.
- [x] **Contratos**: Endpoint protegido para exibição de termos contratuais.
- [x] **Banco de Dados**: Configuração pronta para operações `async/await`.

## 📦 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd projeto-api-bancaria
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco
   SECRET_KEY=sua_chave_secreta_aqui
   ALGORITHM=HS256
   ```

5. **Execute a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```

## 📑 Documentação da API

Após iniciar o servidor, acesse a documentação interativa:
*   **Swagger UI**: [http://127.0.0](http://127.0.0)
*   **Redoc**: [http://127.0.0](http://127.0.0)

## 🏗️ Estrutura do Projeto

```text
├── core/           # Configurações de segurança e banco de dados
├── models/         # Modelos de tabelas do banco de dados (SQLAlchemy)
├── schemas/        # Modelos de validação de dados (Pydantic)
├── routers/        # Rotas e lógica de negócio dividida por módulos
└── main.py         # Ponto de entrada da aplicação
```

---
Desenvolvido por Mariana Miranda (https://github.com)
