from pydantic import BaseModel


class Roles(BaseModel):
    id: int = None
    nombre: str
    estado: bool
