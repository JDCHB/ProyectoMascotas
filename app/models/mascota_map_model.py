from pydantic import BaseModel


class MascotasMap(BaseModel):
    nombre_mascota: str
    latitud: str
    longitud: str