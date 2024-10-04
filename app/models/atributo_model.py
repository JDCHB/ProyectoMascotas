from pydantic import BaseModel


class Atributo(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    estado: bool
