from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    centro_treinamento = Column(String)
    categoria = Column(String)
