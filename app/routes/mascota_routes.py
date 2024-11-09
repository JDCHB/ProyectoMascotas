from fastapi import APIRouter, HTTPException
from app.models.mascotas_model import Mascotas
from app.controllers.mascota_controller import *

router = APIRouter()

nueva_mascota = Mascotacontroller()


@router.get("/get_mascotas_R/")
async def get_mascotas_R():
    rpta = nueva_mascota.get_mascotas_R()
    return rpta

@router.post("/create_mascota")
async def create_mascota(mascota: Mascotas):
    rpta = nueva_mascota.create_mascota(mascota)
    return rpta


@router.get("/get_mascota/{mascota_id}", response_model=Mascotas)
async def get_mascota(mascota_id: int):
    try:
        rpta = nueva_mascota.get_mascota(mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_mascota/{mascota_id}")
async def update_mascota(mascota_id: int, mascota: Mascotas):
    try:
        rpta = nueva_mascota.update_mascota(mascota_id, mascota)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_mascotas/")
async def get_mascotas():
    rpta = nueva_mascota.get_mascotas()
    return rpta


@router.delete("/delete_mascota/{mascota_id}")
async def delete_mascotas(mascota_id: int):
    try:
        rpta = nueva_mascota.delete_mascotas(mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
