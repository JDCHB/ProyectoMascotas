from pydantic import BaseModel


class Mascotas(BaseModel):
    id: int = None
    nombre: str
    id_genero_mascota: int
    id_tipo_mascota: int
    id_propietario: int
    coordenadas: str
    estado: bool
