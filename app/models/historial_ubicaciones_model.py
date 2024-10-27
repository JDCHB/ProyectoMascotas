from pydantic import BaseModel


class Historial_Ubicaciones(BaseModel):
    id: int = None
    id_collar: int = None
    latitud: str
    longitud: str
    distancia_recorrida: str
