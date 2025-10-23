# Workout API - FastAPI + SQLAlchemy + Alembic + Docker

Projeto exemplo para aprendizado de FastAPI com PostgreSQL via Docker, usando SQLAlchemy e Alembic.

Endpoints:
- `GET /atletas/` - listar atletas
- `POST /atletas/` - criar atleta

Docs: http://127.0.0.1:8000/docs

Execute com Docker:
1. `make run-docker`
2. `make run-migrations`
3. `make run`

Ou localmente:
1. Crie um virtualenv e instale `pip install -r requirements.txt`
2. Configure um PostgreSQL e ajuste `app/core/database.py` ou use `DATABASE_URL` env var
3. Rode `uvicorn app.main:app --reload`
