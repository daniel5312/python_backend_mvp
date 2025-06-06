from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str
    rol: str
    finca: str | None = None
    municipio: str | None = None
    vereda: str | None = None
    productos: str | None = None
    etapa: str | None = None
