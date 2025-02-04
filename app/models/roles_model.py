from pydantic import BaseModel


class Roles(BaseModel):
    id: int = None
    nombre: str
    estado: bool


class Actualizar_Estado_Rol(BaseModel):
    id: int = None
    estado: bool
