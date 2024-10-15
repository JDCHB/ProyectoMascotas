from pydantic import BaseModel


class Genero_Mascota(BaseModel):
    id: int = None
    genero: str
    estado: bool
