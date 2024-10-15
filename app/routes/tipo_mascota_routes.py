from fastapi import APIRouter, HTTPException
from app.models.tipo_mascota_model import Tipo_mascota
from app.controllers.roles_controller import *
router = APIRouter()

nuevo_rol = Rolescontroller()


@router.post("/create_tipo_mascota")
async def create_tipo_mascota(tipo_mascota: Tipo_mascota):
    rpta = nuevo_rol.create_tipo_mascota(tipo_mascota)
    return rpta


@router.get("/get_tipo_mascota/{tipo_mascota_id}", response_model=Tipo_mascota)
async def get_tipo_mascota(tipo_mascota_id: int):
    try:
        rpta = nuevo_rol.get_tipo_mascota(tipo_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_todos_tipo_mascota/")
async def get_todos_tipo_mascota():
    rpta = nuevo_rol.get_todos_tipo_mascota()
    return rpta


@router.put("/update_tipo_mascota/{tipo_mascota_id}")
async def update_tipo_mascota(tipo_mascota_id: int, tipo_mascota: Tipo_mascota):
    try:
        rpta = nuevo_rol.update_tipo_mascota(tipo_mascota_id, tipo_mascota)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_tipo_mascota/{tipo_mascota_id}")
async def delete_tipo_mascota(tipo_mascota_id: int):
    try:
        rpta = nuevo_rol.delete_tipo_mascota(tipo_mascota_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
