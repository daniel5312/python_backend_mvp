from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    rol = Column(String(50))
    finca = Column(String(100), nullable=True)
    municipio = Column(String(100), nullable=True)
    vereda = Column(String(100), nullable=True)
    productos = Column(String(255), nullable=True)
    etapa = Column(String(100), nullable=True)