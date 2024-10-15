from fastapi import APIRouter, HTTPException
from app.models.genero_mascota_model import Genero_Mascota
from app.controllers.genero_mascota_controller import *
router = APIRouter()

nuevo_genero_mascota = Genero_Mascotas_controller()


@router.post("/create_genero_mascota")
async def create_genero_mascota(genero_mascota: Genero_Mascota):
    rpta = nuevo_genero_mascota.create_genero_mascota(genero_mascota)
    return rpta


@router.get("/get_genero_mascota/{genero_mascota_id}", response_model=Genero_Mascota)
async def get_genero_mascota(genero_mascota_id: int):
    try:
        rpta = nuevo_genero_mascota.get_genero_mascota(genero_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_todos_genero_mascota/")
async def get_todos_genero_mascota():
    rpta = nuevo_genero_mascota.get_todos_genero_mascota()
    return rpta


@router.put("/update_genero_mascota/{genero_mascota_id}")
async def update_genero_mascota(genero_mascota_id: int, genero_mascota: Genero_Mascota):
    try:
        rpta = nuevo_genero_mascota.update_genero_mascota(
            genero_mascota_id, genero_mascota)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_genero_mascota/{genero_mascota_id}")
async def delete_genero_mascota(genero_mascota_id: int):
    try:
        rpta = nuevo_genero_mascota.delete_genero_mascota(genero_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
