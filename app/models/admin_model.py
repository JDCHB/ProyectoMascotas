from pydantic import BaseModel


class NuevoCollar(BaseModel):
    numero_serie: str
    id_mascota_vinculada: int
    estado: bool
    # Nivel predeterminado si no se especifica
    nivel_bateria: int


class NuevoRol(BaseModel):
    id: int
    nombre: str
    estado: bool


class NuevoModulo(BaseModel):
    id: int
    nombre: str
    estado: bool
