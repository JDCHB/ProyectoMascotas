from pydantic import BaseModel


class MascotasReport(BaseModel):
    fecha1 = str
    fecha2 = str