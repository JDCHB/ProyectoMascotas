from pydantic import BaseModel


class AtributoxUsuario(BaseModel):
    id: int = None
    id_usuario: int = None
    id_atributo: int = None
    valor: str
    descripcion: str
