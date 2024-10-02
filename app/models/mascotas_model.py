from pydantic import BaseModel

class Mascotas(BaseModel):
    id: int = None
    nombre: str
    tipo_mascota: str
    id_propietario: int
    coordenadas: str
    