from fastapi import APIRouter, HTTPException
from app.models.atributoxusuario_model import AtributoxUsuario
from app.controllers.atributoxusuario_controller import *
router = APIRouter()

nuevo_atributoxusuario = AtributoxUsuariocontroller()


@router.post("/create_atributoxusuario")
async def create_atributoxusuario(atributoxusuario: AtributoxUsuario):
    rpta = nuevo_atributoxusuario.create_atributoxusuario(atributoxusuario)
    return rpta


@router.get("/get_atributoxusuario/{atributoxusuario_id}", response_model=AtributoxUsuario)
async def get_atributoxusuario(atributoxusuario_id: int):
    try:
        rpta = nuevo_atributoxusuario.get_atributoxusuario(
            atributoxusuario_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_atributoxusuarios/{atributoxusuario_id}")
async def update_atributoxusuarios(atributoxusuario_id: int, atributoxusuario: AtributoxUsuario):
    try:
        rpta = nuevo_atributoxusuario.update_atributoxusuarios(
            atributoxusuario_id, atributoxusuario)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_atributoxusuarios/")
async def get_atributoxusuarios():
    rpta = nuevo_atributoxusuario.get_atributoxusuarios()
    return rpta


@router.delete("/delete_atributoxusuario/{atributoxusuario_id}")
async def delete_atributoxusuario(atributoxusuario_id: int):
    try:
        rpta = nuevo_atributoxusuario.delete_atributoxusuario(
            atributoxusuario_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
