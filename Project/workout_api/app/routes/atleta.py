from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app import crud, schemas
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/atletas", tags=["Atletas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.atleta.AtletaResponse])
def listar_atletas(db: Session = Depends(get_db)):
    return crud.atleta.get_all(db)

@router.post("/", response_model=schemas.atleta.AtletaResponse, status_code=status.HTTP_201_CREATED)
def criar_atleta(atleta: schemas.atleta.AtletaCreate, db: Session = Depends(get_db)):
    existing = crud.atleta.get_by_cpf(db, atleta.cpf)
    if existing:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    try:
        return crud.atleta.create(db, atleta)
    except IntegrityError:
        # fallback if race condition
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
