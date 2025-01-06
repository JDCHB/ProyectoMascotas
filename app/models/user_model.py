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
    estado: int  # AQUI ESTABA COMO BOOL


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token: str
