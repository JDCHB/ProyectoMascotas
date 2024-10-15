from pydantic import BaseModel


class Tipo_mascota(BaseModel):
    id: int = None
    tp_mascota: str
    estado: bool
