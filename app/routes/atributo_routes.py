from fastapi import APIRouter, HTTPException
from app.models.atributo_model import Atributo
from app.controllers.atributo_controller import *
router = APIRouter()

nuevo_atributo = Atributocontroller()


@router.post("/create_atributo")
async def create_atributo(atributo: Atributo):
    rpta = nuevo_atributo.create_atributo(atributo)
    return rpta


@router.get("/get_atributo/{atributo_id}", response_model=Atributo)
async def get_atributo(atributo_id: int):
    try:
        rpta = nuevo_atributo.get_atributo(atributo_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_atributo/{atributo_id}")
async def update_atributo(atributo_id: int, atributo: Atributo):
    try:
        rpta = nuevo_atributo.get_atributo(atributo_id, atributo)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_atributos/")
async def get_atributos():
    rpta = nuevo_atributo.get_atributos()
    return rpta


@router.delete("/delete_atributo/{atributo_id}")
async def delete_atributo(atributo_id: int):
    try:
        rpta = nuevo_atributo.delete_atributo(atributo_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
