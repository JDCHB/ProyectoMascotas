from pydantic import BaseModel


class NuevoCollar(BaseModel):
    numero_serie: str
    id_mascota_vinculada: int
