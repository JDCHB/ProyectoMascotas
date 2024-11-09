from pydantic import BaseModel


class Mascotas(BaseModel):
    id: int = None
    nombre: str
    id_genero_mascota: int
    id_tipo_mascota: int
    id_propietario: int
    estado: bool

class GetmascotaR(BaseModel):
    fecha1: int
    fecha2: int