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


@router.get("/get_modulos/")
async def get_modulos():
    rpta = nuevo_admin.get_modulos()
    return rpta


@router.post("/create_moduloXrol")
async def create_moduloXrol(moduloxrol: ModuloxRol):
    rpta = nuevo_admin.create_moduloXrol(moduloxrol)
    return rpta
