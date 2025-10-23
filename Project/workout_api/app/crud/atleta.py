from sqlalchemy.orm import Session
from app.models.atleta import Atleta
from app.schemas.atleta import AtletaCreate

def get_all(db: Session):
    return db.query(Atleta).all()

def get_by_cpf(db: Session, cpf: str):
    return db.query(Atleta).filter(Atleta.cpf == cpf).first()

def create(db: Session, atleta: AtletaCreate):
    db_atleta = Atleta(**atleta.dict())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta
