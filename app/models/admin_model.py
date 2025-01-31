from pydantic import BaseModel


class NuevoCollar(BaseModel):
    numero_serie: str
    id_mascota_vinculada: int
    estado: bool
    # Nivel predeterminado si no se especifica
    nivel_bateria: int


class NuevoModulo(BaseModel):
    id: int = None
    nombre_modulo: str
    estado: bool
