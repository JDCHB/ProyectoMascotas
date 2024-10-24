from pydantic import BaseModel


class Collares_GPS(BaseModel):
    id: int = None
    numero_serie: str
    ultima_ubicacion_registrada: str
    nivel_bateria: int
    id_mascota_vinculada: int = None
    estado: bool
