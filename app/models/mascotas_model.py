from pydantic import BaseModel


class Mascotas(BaseModel):
    id: int = None
    nombre: str
    genero: str
    id_tipo_mascota: str
    id_propietario: int
    coordenadas: str
    estado: bool
