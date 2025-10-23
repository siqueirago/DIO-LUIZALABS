from fastapi import FastAPI
from app.routes import atleta
from app.core.database import Base, engine

# Create DB tables (for dev; in production prefer alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout API", version="1.0")

app.include_router(atleta.router)
