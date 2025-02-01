from pydantic import BaseModel


class NuevoCollar(BaseModel):
    numero_serie: str
    id_mascota_vinculada: int
    estado: bool
    # Nivel predeterminado si no se especifica
    nivel_bateria: int


class NuevoModulo(BaseModel):
    nombre_modulo: str
    descripcion: str
    estado: bool


class ModuloxRol(BaseModel):
    id: int = None
    id_modulo: int
    id_rol: int
    estado: bool
