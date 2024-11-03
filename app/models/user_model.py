from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    email: str
    password: str
    nombre: str
    apellido: str
    documento: str
    telefono: str
    id_rol: int
    estado: bool


class Login(BaseModel):
    email: str
    password: str
