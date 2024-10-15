from fastapi import APIRouter, HTTPException
from app.models.tipo_mascota_model import Tipo_mascota
from app.controllers.tipo_mascota_controller import *
router = APIRouter()

nuevo_tipo_mascota = Tipo_Mascota_controller()


@router.post("/create_tipo_mascota")
async def create_tipo_mascota(tipo_mascota: Tipo_mascota):
    rpta = nuevo_tipo_mascota.create_tipo_mascota(tipo_mascota)
    return rpta


@router.get("/get_tipo_mascota/{tipo_mascota_id}", response_model=Tipo_mascota)
async def get_tipo_mascota(tipo_mascota_id: int):
    try:
        rpta = nuevo_tipo_mascota.get_tipo_mascota(tipo_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_todos_tipo_mascota/")
async def get_todos_tipo_mascota():
    rpta = nuevo_tipo_mascota.get_todos_tipo_mascota()
    return rpta


@router.put("/update_tipo_mascota/{tipo_mascota_id}")
async def update_tipo_mascota(tipo_mascota_id: int, tipo_mascota: Tipo_mascota):
    try:
        rpta = nuevo_tipo_mascota.update_tipo_mascota(
            tipo_mascota_id, tipo_mascota)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_tipo_mascota/{tipo_mascota_id}")
async def delete_tipo_mascota(tipo_mascota_id: int):
    try:
        rpta = nuevo_tipo_mascota.delete_tipo_mascota(tipo_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
