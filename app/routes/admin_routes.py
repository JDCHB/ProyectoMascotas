from fastapi import APIRouter, HTTPException
from app.models.admin_model import NuevoCollar, NuevoModulo, ModuloxRol
from app.controllers.admin_controller import *

router = APIRouter()

nuevo_admin = AdminController()


@router.post("/create_collar")
async def create_collar(nuevocollar: NuevoCollar):
    rpta = nuevo_admin.create_collar(nuevocollar)
    return rpta


@router.post("/create_modulo")
async def create_modulo(nuevomodulo: NuevoModulo):
    rpta = nuevo_admin.create_modulo(nuevomodulo)
    return rpta


@router.get("/get_modulo/{modulo_id}", response_model=NuevoModulo)
async def get_modulo(modulo_id: int):
    rpta = nuevo_admin.get_modulo(modulo_id)
    return rpta


@router.get("/get_modulos/")
async def get_modulos():
    rpta = nuevo_admin.get_modulos()
    return rpta


@router.put("/update_modulo/{modulo_id}")
async def update_modulo(modulo_id: int, nuevomodulo: NuevoModulo):
    try:
        rpta = nuevo_admin.update_modulo(modulo_id, nuevomodulo)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_estado_modulo/{modulo_id}")
async def update_estado_modulo(modulo_id: int, nuevomodulo: NuevoModulo):
    try:
        rpta = nuevo_admin.update_estado_modulo(modulo_id, nuevomodulo)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create_moduloXrol")
async def create_moduloXrol(moduloxrol: ModuloxRol):
    rpta = nuevo_admin.create_moduloXrol(moduloxrol)
    return rpta
